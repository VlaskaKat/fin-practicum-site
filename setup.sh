#!/usr/bin/env bash
# One-time setup of rs.fin-academy.net on this server.
# Installs nginx, puts the site from GitHub into /var/www/fin-practicum-site,
# pulls updates from GitHub every 2 minutes and turns on HTTPS.
set -euo pipefail

DOMAIN="rs.fin-academy.net"
REPO="https://github.com/VlaskaKat/fin-practicum-site.git"
DIR="/var/www/fin-practicum-site"

echo "==> Устанавливаю nginx, git и certbot"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq nginx git certbot python3-certbot-nginx >/dev/null

echo "==> Скачиваю сайт с GitHub"
if [ -d "$DIR/.git" ]; then
  git -C "$DIR" pull -q
else
  git clone -q "$REPO" "$DIR"
fi

echo "==> Настраиваю nginx для $DOMAIN"
cat > /etc/nginx/sites-available/$DOMAIN <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN www.$DOMAIN;
    root $DIR;
    index index.html;
    location ~ /\.git { deny all; }
    location / { try_files \$uri \$uri/ /index.html; }
}
EOF
ln -sf /etc/nginx/sites-available/$DOMAIN /etc/nginx/sites-enabled/$DOMAIN
nginx -t
systemctl enable --now nginx
systemctl reload nginx

echo "==> Включаю автообновление с GitHub каждые 2 минуты"
cat > /etc/cron.d/fin-practicum-site <<EOF
*/2 * * * * root git -C $DIR pull -q --ff-only >/dev/null 2>&1
EOF

if command -v ufw >/dev/null && ufw status | grep -q "Status: active"; then
  ufw allow 'Nginx Full' >/dev/null
fi

echo "==> Включаю HTTPS"
if certbot --nginx -d "$DOMAIN" -d "www.$DOMAIN" --non-interactive --agree-tos --register-unsafely-without-email --redirect; then
  echo "Готово: https://$DOMAIN"
else
  echo "Сайт уже работает по http://$DOMAIN"
  echo "HTTPS не включился — скорее всего, DNS-запись rs ещё не обновилась. Запустите эту команду ещё раз через 10–15 минут."
fi

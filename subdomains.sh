#!/usr/bin/env bash
# Sets up pavlova.fin-academy.net and chachina.fin-academy.net.
# Pages live in the pavlova/ and chachina/ folders of this repo and update from GitHub automatically.
set -euo pipefail
DIR="/var/www/fin-practicum-site"

echo "==> Обновляю сайт с GitHub"
git -C "$DIR" pull -q --ff-only

for NAME in pavlova chachina; do
  DOMAIN="$NAME.fin-academy.net"
  echo "==> Настраиваю $DOMAIN"
  cat > /etc/nginx/sites-available/$DOMAIN <<CONF
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN;
    root $DIR/$NAME;
    index index.html;
    location ~ /\.git { deny all; }
    location / { try_files \$uri \$uri/ /index.html; }
}
CONF
  ln -sf /etc/nginx/sites-available/$DOMAIN /etc/nginx/sites-enabled/$DOMAIN
done

nginx -t
systemctl reload nginx

for NAME in pavlova chachina; do
  DOMAIN="$NAME.fin-academy.net"
  echo "==> Включаю HTTPS для $DOMAIN"
  certbot --nginx -d "$DOMAIN" --non-interactive --agree-tos --register-unsafely-without-email --redirect \
    || echo "HTTPS для $DOMAIN не включился, запустите команду ещё раз через 10 минут"
done

echo "Готово: https://pavlova.fin-academy.net и https://chachina.fin-academy.net"

# Сборка сайта pavlova.fin-academy.net
# Запуск из папки pavlova/:  python3 build_pavlova.py
# Страницы: index.html (главная), bot/index.html (бюджет-ассистент), crypto/index.html (курс «Азы криптовалют»)
import os

TG = "https://t.me/katerinavlaska"
IG = "https://instagram.com/pavlova_finance"
BOT = "https://t.me/BudgetAssistantPavlovaBot"
PRACTICUM = "https://rs.fin-academy.net/"

TGSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M21.9 4.3 18.7 19.4c-.2 1.1-.9 1.3-1.8.8l-4.8-3.6-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.9 8.9-8c.4-.3-.1-.5-.6-.2L6.4 13.2l-4.7-1.5c-1-.3-1-1 .2-1.5L20.6 3c.9-.3 1.6.2 1.3 1.3z"/></svg>'
IGSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
BTC = '<svg viewBox="0 0 64 64" aria-hidden="true"><path fill="currentColor" d="M46.1 27.4c.6-4.3-2.6-6.6-7.1-8.1l1.5-5.8-3.5-.9-1.4 5.7c-.9-.2-1.9-.5-2.8-.7l1.4-5.7-3.5-.9-1.5 5.8c-.8-.2-1.5-.3-2.2-.5l-4.9-1.2-.9 3.8s2.6.6 2.6.6c1.4.4 1.7 1.3 1.6 2l-1.7 6.7c.1 0 .2.1.4.1l-.4-.1-2.3 9.4c-.2.4-.6 1.1-1.6.8 0 0-2.6-.6-2.6-.6l-1.8 4 4.6 1.2c.9.2 1.7.4 2.5.6l-1.5 5.9 3.5.9 1.5-5.8c1 .3 1.9.5 2.8.7l-1.4 5.8 3.5.9 1.5-5.9c6 1.1 10.5.7 12.4-4.8 1.5-4.4-.1-6.9-3.2-8.6 2.3-.5 4-2 4.5-5.1zm-8 11.2c-1.1 4.4-8.4 2-10.8 1.4l1.9-7.7c2.4.6 10 1.8 8.9 6.3zm1.1-11.3c-1 4-7.1 2-9.1 1.5l1.7-7c2 .5 8.4 1.4 7.4 5.5z"/></svg>'

import re as _re
BTC_D = _re.search(r'd="([^"]+)"', BTC).group(1)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=PT+Serif:ital,wght@0,700;1,400&display=swap" rel="stylesheet">'

CSS = r"""
:root{--ink:#15254a;--ink-2:#1d305c;--ink-3:#283d6e;--blue:#3f5d9c;--blue-2:#5675b5;--cyan:#a3bce6;
--bg:#f2f4f9;--card:#fff;--line:#dfe4f0;--text:#1d2340;--muted:#5d647f}
*{box-sizing:border-box;margin:0;padding:0}
html{overflow-x:hidden;scroll-behavior:smooth;scroll-padding-top:84px}
body{font-family:Onest,system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}img{display:block;max-width:100%}
h1,h2,h3{font-family:"PT Serif",Cambria,Georgia,serif;font-weight:700;line-height:1.12;color:var(--ink)}
h2{font-size:clamp(28px,3.8vw,42px);text-transform:uppercase;letter-spacing:.01em;margin-bottom:14px;max-width:24ch}
h3{font-size:20px}
.wrap{max-width:1140px;margin:0 auto;padding:0 24px;position:relative;z-index:1}
section{padding:96px 0;position:relative;overflow:hidden}
.kicker{display:flex;align-items:center;gap:10px;font-size:12.5px;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--blue);margin-bottom:16px}
.kicker::before{content:"";width:10px;height:10px;background:var(--blue);border-radius:2px}
.dark .kicker{color:var(--cyan)}.dark .kicker::before{background:var(--cyan)}
.sub{color:var(--muted);font-size:18px;max-width:62ch;margin-bottom:44px}
.dark{background:var(--ink);color:#fff;overflow:hidden}
.dark h2,.dark h3{color:#fff}.dark .sub{color:rgba(255,255,255,.7)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;font:600 16px/1 Onest,sans-serif;text-decoration:none;padding:17px 28px;border-radius:12px;transition:background .25s,box-shadow .25s,transform .25s,color .25s;cursor:pointer;border:0}
.btn svg{width:19px;height:19px}
.btn-blue{background:var(--blue);color:#fff;box-shadow:0 12px 30px -10px rgba(63,93,156,.75)}
.btn-blue:hover{background:var(--blue-2);transform:translateY(-2px)}
.btn-ghost{color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.35)}
.btn-ghost:hover{box-shadow:inset 0 0 0 1px #fff;background:rgba(255,255,255,.06)}
.btn-line{color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--ink)}.btn-line:hover{background:var(--ink);color:#fff}

/* header */
header{position:fixed;inset:0 0 auto;z-index:50;background:rgba(21,37,74,.9);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.08)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:20px;color:#fff}
.brand{text-decoration:none;line-height:1.2;display:flex;align-items:center;gap:12px}
.brand .mark{width:38px;height:38px;border-radius:10px;background:var(--blue);display:grid;place-items:center;font-family:"PT Serif",serif;font-weight:700;font-size:17px}
.brand b{font-family:"PT Serif",serif;font-size:18px;display:block}
.brand span{font-size:12.5px;color:rgba(255,255,255,.6)}
.nav ul{display:flex;gap:22px;list-style:none;font-size:15px;white-space:nowrap}
.nav ul a{text-decoration:none;color:rgba(255,255,255,.72);transition:color .2s;padding:6px 0;border-bottom:2px solid transparent}
.nav ul a:hover{color:#fff}.nav ul a.on{color:#fff;border-color:var(--cyan)}
.nav .btn{padding:11px 18px;font-size:15px}
.burger{display:none;background:none;border:0;color:#fff;width:40px;height:40px;cursor:pointer}
.burger svg{width:26px;height:26px}
@media(max-width:1100px){.nav ul{display:none;position:absolute;top:72px;left:0;right:0;flex-direction:column;gap:0;background:var(--ink);padding:10px 24px 20px;border-bottom:1px solid rgba(255,255,255,.1)}
.nav ul.open{display:flex}.nav ul a{display:block;padding:12px 0}.burger{display:block}}
@media(max-width:520px){.nav .btn{display:none}.brand span{display:none}}

/* bitcoin background */
.btc-bg{position:absolute;pointer-events:none;color:#fff;opacity:.025;filter:blur(1.5px);z-index:0;animation:float 22s ease-in-out infinite}
.btc-bg svg{width:100%;height:100%}
.light .btc-bg{color:var(--ink);opacity:.018}
@keyframes float{0%,100%{transform:translateY(0) rotate(-2deg)}50%{transform:translateY(-20px) rotate(2deg)}}
@keyframes spin{to{transform:rotate(360deg)}}
.sym{position:absolute;z-index:0;pointer-events:none;user-select:none;font-family:"PT Serif",Georgia,serif;font-weight:700;line-height:1;color:#fff;opacity:.03;filter:blur(1.5px);animation-name:drift,sway;animation-timing-function:ease-in-out;animation-iteration-count:infinite;animation-direction:alternate}
.sym.b{opacity:.022}
section.light .sym{color:var(--ink);opacity:.02}section.light .sym.b{opacity:.014}
@keyframes drift{from{transform:translate(0,0) rotate(-3deg)}to{transform:translate(30px,-50px) rotate(3deg)}}
@keyframes sway{from{margin-left:-20px}to{margin-left:30px}}

/* hero */
.hero{background:radial-gradient(900px 520px at 85% 0%,rgba(63,93,156,.45),transparent 60%),radial-gradient(700px 500px at 0% 100%,rgba(163,188,230,.12),transparent 60%),var(--ink);color:#fff;padding:150px 0 0;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.3fr .7fr;padding-bottom:0;gap:40px;align-items:end;position:relative;z-index:1}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:14px;color:var(--cyan);border:1px solid rgba(163,188,230,.3);padding:8px 16px;border-radius:999px;margin-bottom:26px}
.eyebrow i{width:8px;height:8px;border-radius:50%;background:var(--cyan);box-shadow:0 0 0 4px rgba(163,188,230,.2);animation:pulse 2s infinite}
@keyframes pulse{50%{box-shadow:0 0 0 8px rgba(163,188,230,0)}}
.hero h1{color:#fff;font-size:clamp(30px,4.2vw,48px);text-transform:uppercase;max-width:15ch;margin-bottom:22px}
.hero .lead{font-family:"PT Serif",serif;font-style:italic;font-size:clamp(19px,2vw,23px);color:rgba(255,255,255,.85);max-width:34ch;margin-bottom:36px}
.hero-btns{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:56px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid rgba(255,255,255,.14);padding:26px 0 40px;gap:20px}
.stats b{font-family:"PT Serif",serif;font-size:36px;color:var(--cyan);display:block;line-height:1.1}
.stats span{font-size:14px;line-height:1.4;display:block;color:rgba(255,255,255,.65)}
.photo{position:relative;align-self:start;justify-self:center;margin-bottom:56px;width:100%;max-width:320px}
.photo::before{display:none;content:"";position:absolute;inset:-18px -18px auto auto;width:70%;height:70%;border:1.5px solid rgba(163,188,230,.45);border-radius:20px}
.photo img{position:relative;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;border-radius:20px;box-shadow:0 0 70px -10px rgba(110,145,220,.55),0 0 0 1px rgba(150,180,240,.15)}
.photo .badge{position:absolute;left:-26px;bottom:40px;background:#fff;color:var(--ink);border-radius:14px;padding:12px 16px;display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600;box-shadow:0 18px 40px -12px rgba(0,0,0,.5);animation:float2 6s ease-in-out infinite}
.photo .badge svg{width:30px;height:30px;color:#f7931a}
@keyframes float2{50%{transform:translateY(-10px)}}
@media(max-width:860px){.hero-grid{grid-template-columns:1fr;gap:0}.hero .hero-btns{margin-bottom:32px}.photo{max-width:280px}.stats{grid-template-columns:1fr 1fr 1fr}.stats b{font-size:28px}}

/* page hero (inner pages) */
.phero{padding:150px 0 80px}
.phero h1{font-size:clamp(34px,5vw,58px);max-width:18ch}
.phero .hero-btns{margin:0}
.phero-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:48px;align-items:center;position:relative;z-index:1}
@media(max-width:860px){.phero-grid{grid-template-columns:1fr}}

/* cards */
.grid{display:grid;gap:22px}
.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:900px){.g3,.g4{grid-template-columns:1fr 1fr}}
@media(max-width:620px){.g2,.g3,.g4{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:28px;transition:transform .3s,box-shadow .3s}
.card:hover{transform:translateY(-4px);box-shadow:0 24px 50px -24px rgba(21,37,74,.35)}
.card h3{margin-bottom:8px}
.card p{color:var(--muted);font-size:16px}
.card .ic{width:46px;height:46px;border-radius:12px;background:rgba(63,93,156,.1);color:var(--blue);display:grid;place-items:center;margin-bottom:18px;font-weight:700;font-family:"PT Serif",serif;font-size:18px}
.card .ic svg{width:24px;height:24px}
.card.ink{background:var(--ink-2);border-color:var(--ink-2);color:#fff}.card.ink h3{color:#fff}.card.ink p{color:rgba(255,255,255,.72)}
.dark .card{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1)}
.dark .card p{color:rgba(255,255,255,.7)}.dark .card .ic{background:rgba(163,188,230,.12);color:var(--cyan)}

/* about */
.about{display:block}
.about img{border-radius:20px;width:100%;max-width:320px;box-shadow:0 24px 50px -24px rgba(21,37,74,.4);aspect-ratio:4/5;object-fit:cover;object-position:top}
.about ul{list-style:none;display:grid;gap:14px;margin-top:8px}
.about li{display:flex;gap:14px;font-size:17px}
.about li svg{flex:none;width:22px;height:22px;color:var(--blue);margin-top:2px}
@media(max-width:860px){.about{grid-template-columns:1fr;gap:28px}.about img{max-width:260px;justify-self:center}.photo .badge{left:-8px}}

/* services teaser */
.feat{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
@media(max-width:760px){.feat{grid-template-columns:1fr}}
.feat a{display:block;text-decoration:none;border-radius:22px;padding:36px;position:relative;overflow:hidden;min-height:300px;transition:transform .3s}
.feat a:hover{transform:translateY(-5px)}
.feat .f1{background:linear-gradient(140deg,var(--ink-2),var(--ink));color:#fff}
.feat .f2{background:linear-gradient(140deg,var(--blue),#2c4682);color:#fff}
.feat h3{color:#fff;font-size:26px;text-transform:uppercase;margin:14px 0 10px;max-width:16ch}
.feat p{color:rgba(255,255,255,.78);max-width:36ch;margin-bottom:22px}
.feat .tag{display:inline-block;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--cyan)}
.feat .f2 .tag{color:#fff;opacity:.85}
.feat .more{font-weight:600;display:inline-flex;gap:8px;align-items:center}
.feat .more::after{content:"→";transition:transform .25s}.feat a:hover .more::after{transform:translateX(5px)}
.prk{padding:44px;display:grid;grid-template-columns:1fr auto;gap:30px;align-items:center}.prk .btn{white-space:nowrap}
@media(max-width:860px){.prk{grid-template-columns:1fr;padding:30px 24px}.prk .btn{white-space:normal;width:100%}}
.feat .big{position:absolute;right:-30px;bottom:-40px;width:220px;height:220px;opacity:.1;color:#fff}
.feat .big svg{width:100%;height:100%}
.feat a:hover .big{animation:spin 12s linear infinite}

/* questions */
.qs{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.qs div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px 18px 50px;position:relative;font-size:16.5px}
.qs div::before{content:"?";position:absolute;left:16px;top:16px;width:24px;height:24px;border-radius:50%;background:var(--blue);color:#fff;font-size:14px;font-weight:700;display:grid;place-items:center}
@media(max-width:760px){.qs{grid-template-columns:1fr}}

.club{background:var(--ink);color:#fff;background-image:radial-gradient(900px 500px at 0% 0%,rgba(86,117,181,.35),transparent 60%)}
.club h2{color:#fff}.club .sub{color:rgba(255,255,255,.72)}.club .kicker{color:var(--cyan)}.club .kicker::before{background:var(--cyan)}
.club-card{display:grid;grid-template-columns:300px 1fr;border-radius:26px;overflow:hidden;border:1px solid rgba(163,188,230,.35);box-shadow:0 30px 70px -30px rgba(110,145,220,.6)}
.club-side{padding:34px 30px;background:linear-gradient(160deg,var(--blue),var(--blue-2) 60%,var(--cyan));color:#fff;display:flex;flex-direction:column}
.club-side .t{font-size:14px;font-weight:600;margin-bottom:12px}
.club-side .cp{font-family:"PT Serif",Georgia,serif;font-size:46px;font-weight:700;line-height:1}
.club-side .cp small{font-family:inherit;font-size:17px;font-weight:600}
.club-side .eur{margin:10px 0 22px;font-weight:600}
.club-note{font-size:14.5px;line-height:1.5;font-weight:500;background:rgba(21,37,74,.25);border-radius:14px;padding:12px 14px;margin-bottom:20px}
.club-side .btn{margin-top:auto;background:var(--ink);color:#fff;width:100%}
.club-side .more{margin-top:14px;font-size:14.5px;font-weight:600;color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.5);align-self:flex-start}
.club-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;padding:26px;background:var(--ink-2)}
.ct{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:18px 20px}
.ct b{display:block;color:var(--cyan);font-size:16.5px;margin-bottom:6px}
.ct p{font-size:15px;color:rgba(255,255,255,.75);line-height:1.5}
@media(max-width:900px){.club-card{grid-template-columns:1fr}.club-grid{grid-template-columns:1fr}}
/* prices */
.prices{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-bottom:22px}
@media(max-width:900px){.prices{grid-template-columns:1fr}}
.price{background:#fff;border:1px solid var(--line);border-radius:18px;padding:30px;display:flex;flex-direction:column;position:relative}
.prices.p4{grid-template-columns:repeat(4,1fr)}@media(max-width:1100px){.prices.p4{grid-template-columns:1fr 1fr}}@media(max-width:600px){.prices.p4{grid-template-columns:1fr}}
.prices.p2{grid-template-columns:repeat(2,1fr);max-width:760px}@media(max-width:700px){.prices.p2{grid-template-columns:1fr}}
.price.pop{border:2px solid var(--blue)}
.price .lbl{position:absolute;top:-13px;left:24px;background:var(--blue);color:#fff;font-size:12.5px;font-weight:700;padding:5px 12px;border-radius:999px}
.price h3{margin-bottom:6px}
.price .val{font-family:"PT Serif",serif;font-size:38px;font-weight:700;color:var(--ink);line-height:1.1;margin:12px 0 4px}
.price .dur{color:var(--muted);font-size:15px;margin-bottom:14px}
.price p{color:var(--muted);font-size:16px;margin-bottom:22px;flex:1}
.price .btn{width:100%}
.plans{display:grid;grid-template-columns:1fr 1.3fr;gap:22px}
@media(max-width:900px){.plans{grid-template-columns:1fr}}
.plan{border-radius:20px;padding:34px;background:#fff;border:1px solid var(--line);display:flex;flex-direction:column}
.plan.ink{background:var(--ink);color:#fff;border-color:var(--ink)}
.plan.ink h3,.plan.ink .val{color:#fff}
.plan .val{font-family:"PT Serif",serif;font-size:40px;font-weight:700;color:var(--ink);margin:10px 0 2px}
.plan .dur{opacity:.7;font-size:15px;margin-bottom:18px}
.plan .tag{display:inline-block;align-self:flex-start;font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--cyan);border:1px solid rgba(163,188,230,.4);border-radius:999px;padding:5px 12px;margin-bottom:14px}
.plan ul{list-style:none;display:grid;gap:10px;margin-bottom:26px;flex:1;align-content:start}
.plan li{display:flex;gap:12px;font-size:16px}
.plan li svg{flex:none;width:20px;height:20px;color:var(--blue);margin-top:3px}
.plan.ink li svg{color:var(--cyan)}

/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;counter-reset:s}
@media(max-width:860px){.steps{grid-template-columns:1fr}}
.steps div{counter-increment:s;padding-top:20px;border-top:2px solid var(--blue)}
.steps div::before{content:"0" counter(s);font-family:"PT Serif",serif;font-weight:700;font-size:30px;color:var(--blue);display:block;margin-bottom:6px}
.steps h3{margin-bottom:6px}.steps p{color:var(--muted)}
.dark .steps div{border-color:var(--cyan)}.dark .steps div::before{color:var(--cyan)}.dark .steps p{color:rgba(255,255,255,.7)}

/* lessons */
.lessons{display:grid;gap:16px}
.lesson{background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden}
.lesson summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:70px 1fr 30px;gap:16px;align-items:center;padding:22px 26px}
.lesson summary::-webkit-details-marker{display:none}
.lesson .n{font-family:"PT Serif",serif;font-weight:700;font-size:32px;color:var(--blue);line-height:1}
.lesson summary h3{font-size:21px;text-transform:uppercase}
.lesson summary small{display:block;color:var(--muted);font-size:15px;margin-top:4px;font-family:Onest,sans-serif;text-transform:none;font-weight:400}
.lesson .pl{width:30px;height:30px;border-radius:50%;background:var(--bg);display:grid;place-items:center;color:var(--blue);font-size:20px;font-weight:600;transition:transform .3s}
.lesson[open] .pl{transform:rotate(45deg);background:var(--blue);color:#fff}
.lesson .body{padding:0 26px 26px 112px;display:grid;grid-template-columns:1.4fr 1fr;gap:26px}
.lesson ul{list-style:none;display:grid;gap:8px}
.lesson ul li{display:flex;gap:10px;font-size:16px}
.lesson ul li::before{content:"";flex:none;width:7px;height:7px;border-radius:2px;background:var(--blue);margin-top:10px}
.lesson .prac{background:var(--bg);border-radius:14px;padding:18px 20px;font-size:15.5px;align-self:start}
.lesson .prac b{display:block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
@media(max-width:760px){.lesson summary{grid-template-columns:44px 1fr 30px;padding:18px}.lesson .n{font-size:24px}.lesson .body{grid-template-columns:1fr;padding:0 18px 20px}}

/* results */
.results{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
@media(max-width:900px){.results{grid-template-columns:1fr 1fr}}
.results div{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:22px 18px;text-align:center;font-weight:600;font-size:16px}
.results div i{display:grid;place-items:center;width:52px;height:52px;margin:0 auto 12px;border-radius:50%;background:rgba(163,188,230,.12);color:var(--cyan);font-style:normal;font-size:22px}

.shot{width:100%;max-width:300px;height:auto;margin:0 auto;border-radius:30px;box-shadow:0 40px 80px -30px rgba(0,0,0,.7),0 0 0 6px #101d3c,0 0 0 7px rgba(255,255,255,.12);position:relative;z-index:1}
/* mock phone (bot) */
.phone{background:#101d3c;border-radius:34px;padding:14px;max-width:330px;margin:0 auto;box-shadow:0 40px 80px -30px rgba(0,0,0,.7),inset 0 0 0 1px rgba(255,255,255,.1);position:relative;z-index:1}
.chat{background:linear-gradient(#1b2d58,#14244a);border-radius:24px;padding:18px 14px;display:grid;gap:10px;min-height:420px;align-content:end}
.chat .top{display:flex;align-items:center;gap:10px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.08);margin-bottom:auto;color:#fff;font-size:14px;font-weight:600}
.chat .top i{width:32px;height:32px;border-radius:50%;background:var(--blue);display:grid;place-items:center;font-style:normal;font-size:15px}
.chat .top small{display:block;font-weight:400;color:rgba(255,255,255,.5);font-size:12px}
.msg{max-width:84%;padding:10px 13px;border-radius:14px;font-size:14px;line-height:1.45;opacity:0;transform:translateY(10px);animation:msg .5s forwards}
.msg.me{justify-self:end;background:var(--blue);color:#fff;border-bottom-right-radius:4px}
.msg.bot{justify-self:start;background:rgba(255,255,255,.08);color:#fff;border-bottom-left-radius:4px}
.msg.voice{display:flex;align-items:center;gap:8px}
.msg.voice span{display:flex;gap:2px;align-items:center}
.msg.voice span i{width:3px;background:#fff;border-radius:2px;animation:wave 1s ease-in-out infinite}
@keyframes wave{50%{transform:scaleY(.4)}}
@keyframes msg{to{opacity:1;transform:none}}

/* misc */
.cta{text-align:center}
.cta h2{margin:0 auto 14px;max-width:30ch;font-size:clamp(22px,2.6vw,30px);text-transform:none;letter-spacing:0;font-weight:700;line-height:1.25}.cta .sub{margin:0 auto 34px}
.cta .hero-btns{justify-content:center;margin:0}
.note{font-size:14.5px;color:var(--muted);margin-top:18px}
.pill{display:inline-flex;align-items:center;gap:8px;background:rgba(63,93,156,.1);color:var(--blue);font-weight:600;font-size:14px;padding:7px 14px;border-radius:999px}
.dark .pill{background:rgba(163,188,230,.12);color:var(--cyan)}
.pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}

/* glow like fin-academy */
.card,.plan,.qs div,.lesson,.results div,.feat a,.prk{box-shadow:0 26px 60px -32px rgba(86,117,181,.55),0 0 0 1px rgba(120,150,210,.08)}
.card:hover,.plan:hover,.feat a:hover,.qs div:hover{box-shadow:0 30px 70px -26px rgba(86,117,181,.7),0 0 0 1px rgba(120,150,210,.18)}
.dark .card,.dark .results div,.feat a,.prk{box-shadow:0 30px 70px -30px rgba(110,145,220,.6),0 0 0 1px rgba(150,180,240,.12)}
.btn-blue{box-shadow:0 10px 30px -10px rgba(110,145,220,.75)}
.btn-blue:hover{box-shadow:0 14px 36px -10px rgba(110,145,220,.9)}
.about img{box-shadow:0 30px 70px -28px rgba(86,117,181,.7),0 0 0 1px rgba(120,150,210,.12)!important}
.phone{box-shadow:0 40px 80px -30px rgba(0,0,0,.6),0 0 60px -10px rgba(110,145,220,.35),inset 0 0 0 1px rgba(255,255,255,.1)}
.qs div,.plan,.feat a{transition:transform .3s,box-shadow .3s}
.ava{width:54px;height:54px;border-radius:50%;margin-bottom:14px;box-shadow:0 8px 20px -8px rgba(21,37,74,.45)}
.price .ava{position:absolute;top:22px;right:22px;width:46px;height:46px;margin:0}.price .ava~h3{padding-right:50px}
.eyebrow img{width:26px;height:26px;border-radius:50%;margin-left:-8px}
.grp{font-size:clamp(20px,2.2vw,26px);margin:56px 0 6px}
.intro{font-size:18px;max-width:70ch;margin-bottom:26px;line-height:1.65}
.bio{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}@media(max-width:760px){.bio{grid-template-columns:1fr}}
.bio p{background:#fff;border-radius:14px;padding:16px 20px;font-size:16.5px;border:1px solid var(--line);box-shadow:0 6px 22px -8px rgba(86,117,181,.35)}
footer{background:#101d3c;color:rgba(255,255,255,.6);padding:40px 0;font-size:14.5px}
.foot{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:center}
.foot .soc{display:flex;gap:12px}
.foot .soc a{width:40px;height:40px;border-radius:10px;background:rgba(255,255,255,.07);display:grid;place-items:center;color:#fff;transition:background .2s}
.foot .soc a:hover{background:var(--blue)}.foot .soc svg{width:19px;height:19px}
.fade{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}
.fade.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.fade{opacity:1;transform:none}}
"""

JS = r"""
<script>
(function(){
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.fade').forEach(function(el){io.observe(el)});
var b=document.querySelector('.burger'),u=document.querySelector('.nav ul');
if(b)b.onclick=function(){u.classList.toggle('open')};
document.querySelectorAll('.nav ul a').forEach(function(a){a.onclick=function(){u.classList.remove('open')}});
// floating ₿ € $ symbols
var BSVG='<svg viewBox="0 0 64 64" width="1em" height="1em"><path fill="currentColor" d="'+document.querySelector('#btcpath').getAttribute('d')+'"/></svg>';
var SY=['₿','€','$','₿','€','$','₿'];
document.querySelectorAll('.hero,.dark,section.light').forEach(function(sec,k){
  var n=sec.classList.contains('light')?5:9;
  for(var i=0;i<n;i++){var e=document.createElement('span');e.className='sym';
    var ch=SY[(i+k)%SY.length];if(ch==='₿'){e.classList.add('b');e.innerHTML=BSVG}else e.textContent=ch;
    var sz=40+Math.random()*(i%3===0?200:90);
    e.style.cssText='font-size:'+sz+'px;left:'+(Math.random()*96)+'%;top:'+(Math.random()*90)+'%;animation-duration:'+(26+Math.random()*20)+'s,'+(30+Math.random()*20)+'s;animation-delay:-'+(Math.random()*20)+'s,-'+(Math.random()*20)+'s';
    sec.insertBefore(e,sec.firstChild)}
});
})();
</script>
"""

def btc_bg(size, top, side, val, delay=0, extra=''):
    return f'<div class="btc-bg" style="width:{size}px;height:{size}px;top:{top};{side}:{val};animation-delay:-{delay}s{extra}">{BTC}</div>'

def header(active, root):
    items = [('index', 'Главная', root), ('about', 'Обо мне', root + '#about'), ('services', 'Услуги', root + '#services'),
             ('bot', 'Бюджет-бот', root + 'bot/'), ('crypto', 'Азы криптовалют', root + 'crypto/'), ('club', 'Финансовый клуб', root + '#club'), ('contacts', 'Контакты', '#contacts')]
    lis = ''.join(f'<li><a href="{h}"{" class=on" if k == active else ""}>{t}</a></li>' for k, t, h in items if k != 'index')
    return f'''<header><div class="wrap nav">
<a class="brand" href="{root}"><span class="mark">ЕП</span><span><b>Екатерина Павлова</b><span>Международный финансовый советник</span></span></a>
<ul>{lis}</ul>
<div style="display:flex;gap:10px;align-items:center"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Записаться</a>
<button class="burger" aria-label="Меню"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div>
</div></header>'''

def footer():
    return f'''<section class="dark cta" id="contacts">

<div class="wrap fade">
<div class="kicker" style="justify-content:center">Контакты</div>
<h2>Начните с бесплатной встречи&#8209;знакомства</h2>
<p class="sub">30 минут онлайн: разберём ваш вопрос и подберём формат. Пишите в Telegram или Instagram, отвечаю лично.</p>
<div class="hero-btns"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Telegram @katerinavlaska</a>
<a class="btn btn-ghost" href="{IG}" target="_blank" rel="noopener">{IGSVG}Instagram @pavlova_finance</a></div>
</div></section>
<footer><div class="wrap foot"><span>© 2026 Екатерина Павлова · Международный финансовый советник · Нови-Сад, Сербия</span>
<div class="soc"><a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{TGSVG}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IGSVG}</a></div></div></footer>'''

def page(title, desc, active, root, body):
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8"><meta http-equiv="Cache-Control" content="no-cache, must-revalidate">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://pavlova.fin-academy.net/ekaterina.jpg">
<meta name="theme-color" content="#15254a">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{header(active, root)}
{body}
{footer()}
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><path id="btcpath" d="{BTC_D}"/></svg>
{JS}
</body>
</html>
'''

def li(items):
    return ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t in items)

# ---------------- MAIN ----------------
bio = ['Более 25 лет в корпоративных финансах, последние 15 лет на руководящих должностях в крупных корпорациях (X5 Retail Group, Glencore)',
       'Дипломированный специалист по личным финансам и международному финансовому планированию',
       'Высшая школа финансового директора — диплом «Финансовый директор»; Logic Planning Group (США) — финансовое планирование и страхование',
       'Эксперт в сфере криптовалют: создаю безопасные стратегии для роста капитала, автор курса «Азы криптовалют»',
       'Сооснователь клуба «Денежный поток» и практикума «Путь к финансовой свободе», создатель Telegram-бота «Бюджет с Павловой» для учёта финансов',
       'Работаю с клиентами по всему миру, помогаю создавать пассивный доход и достигать финансовых целей',
       'Больше 50 клиентов уже понимают свои финансы и идут к своим целям', 'Инвестор, мама двоих подростков']

qs = ['С чего начать инвестировать, если я живу за рубежом?',
      'Как безопасно купить первую криптовалюту и где её хранить?',
      'Как платить налоги с инвестиций и криптовалюты в Сербии?',
      'Какого брокера выбрать с российским паспортом?',
      'Как вести семейный бюджет в нескольких валютах?',
      'Хорошо зарабатываю, но всё трачу — как начать откладывать?',
      'Как собрать подушку безопасности и защитить семью страховкой?',
      'Как создать свою «пенсионную систему», если на госпенсию рассчитывать не приходится?',
      'Как перевести деньги между странами, в том числе через криптовалюту?',
      'Верна ли моя стратегия и куда двигаться дальше?']

svc_groups = [
 ('Разовые консультации', 'Когда нужен ответ на конкретный вопрос или взгляд со стороны.', [
  ('Встреча-знакомство', 'Бесплатно', '30 минут', 'Обсудим ваш запрос и подберём подходящий формат.', 'Записаться', TG, True),
  ('Консультация', '€150', '60 минут', 'Ответ на ваш конкретный вопрос.', 'Записаться', TG, False),
  ('Аудит финансов', '€150', '90 минут', 'Взгляд со стороны и письменные рекомендации.', 'Записаться', TG, False),
  ('Настройка бота и бюджета', '€50', 'личная встреча', 'Настроим бюджет-ассистента, статьи бюджета и валюты.', 'Записаться', TG, False)]),
 ('Долгосрочная работа', 'Когда нужен не один ответ, а система: стратегия, план и поддержка.', [
  ('Стратегическая сессия', '€500', '2 встречи', 'Разбор вашей ситуации и личная стратегия.', 'Записаться', TG, False),
  ('Финансовый план', 'от €1 500', '5 встреч за 2 месяца', 'Полный план, подбор инструментов и поддержка во внедрении.', 'Записаться', TG, True),
  ('Практикум «Путь к финансовой свободе»', 'от €85', 'вместе с Анной Чачиной', 'Личные финансы и инвестиции для резидентов Сербии: 6 модулей с практикой.', 'Подробнее', PRACTICUM, False),
  ('Финансовый клуб', '€33', 'в месяц', 'Закрытый чат с ответами, бот бесплатно, шаблоны, скидка 30%.', 'Подробнее', 'club/', False)]),
 ('Мои продукты', 'Инструменты, которыми можно пользоваться самостоятельно.', [
  ('Бюджет-ассистент', '€9', 'в месяц или €90 за год', 'Telegram-бот и Google-таблица с дашбордом. Первый месяц бесплатно.', 'Подробнее', 'bot/', False),
  ('Курс «Азы криптовалют»', '€390', 'Чёрная пятница: вместо €500, до 30 ноября', 'Живые уроки, тест после каждого урока и поддержка в чате.', 'Подробнее', 'crypto/', False)])]

def svc_card(n, v, d, t, b, href, pop):
    ext = '' if not href.startswith('http') else ' target="_blank" rel="noopener"'
    small = ' style="font-size:24px"' if len(v) > 10 else ''
    return f'''<div class="price{' pop' if pop else ''} fade">{'<span class="lbl">Начните здесь</span>' if n == 'Встреча-знакомство' else ''}{'<span class="lbl">Максимум результата</span>' if n == 'Финансовый план' else ''}
{'<img class="ava" src="bot/bot-avatar.png" alt="">' if n in ('Настройка бота и бюджета', 'Бюджет-ассистент') else ''}<h3>{n}</h3><div class="val"{small}>{v}</div><div class="dur">{d}</div><p>{t}</p>
<a class="btn {'btn-blue' if pop else 'btn-line'}" href="{href}"{ext}>{b}</a></div>'''

svc_html = ''.join(f'''<h3 class="fade grp">{g}</h3><p class="sub fade" style="margin-bottom:26px">{gd}</p>
<div class="prices p4">{''.join(svc_card(*c) for c in cards)}</div>''' for g, gd, cards in svc_groups)

main_body = f'''
<section class="hero">


<div class="wrap hero-grid">
<div>
<div class="eyebrow"><i></i>Международный финансовый советник</div>
<h1>Превращаю доход в капитал</h1>
<p class="lead">Помогаю навести порядок в деньгах и выстроить устойчивую систему личных финансов — в любой стране мира</p>
<div class="hero-btns"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Бесплатная встреча 30 минут</a><a class="btn btn-ghost" href="#services">Форматы работы</a></div>
</div>
<div class="photo"><img src="ekaterina.jpg" alt="Екатерина Павлова"></div>
</div></section>

<section class="light" id="about">

<div class="wrap about">
<div class="fade">
<div class="kicker">О себе</div>
<h2>Екатерина Павлова</h2>
<p class="sub" style="margin-bottom:14px">Международный финансовый советник, инвестор, игропрактик</p>
<p class="intro">Больше 25 лет я работаю в финансах, из них 15 лет руководила финансами в крупных компаниях. С 2023 года живу в Сербии, в Нови-Саде, и на себе знаю, как устроены деньги, банки и налоги после переезда. Сейчас помогаю русскоязычным семьям по всему миру навести порядок в деньгах, защитить их и превратить доход в капитал.</p>
<div class="bio">{"".join(f"<p>{b}</p>" for b in bio)}</div>
</div></div></section>

<section class="dark">

<div class="wrap">
<div class="kicker fade">Мои продукты</div>
<h2 class="fade">Инструменты, которые я сделала для вас</h2>
<p class="sub fade">Удобный учёт и понятное обучение — с этого начинается порядок в деньгах.</p>
<div class="feat">
<a class="f1 fade" href="bot/"><img class="ava" src="bot/bot-avatar.png" alt="" style="width:64px;height:64px"><span class="tag">Telegram-бот</span><h3>Бюджет-ассистент</h3><p>Записываете траты голосом в любой валюте. Бот пересчитает их в две ваши валюты и занесёт в Google-таблицу с дашбордом.</p><span class="more">Подробнее о боте</span><div class="big"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="26" fill="none" stroke="currentColor" stroke-width="3"/><path d="M32 14v18l12 8" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></div></a>
<a class="f2 fade" href="crypto/"><span class="tag">Авторский курс · до 5 человек</span><h3>Азы криптовалют</h3><p>Живые уроки в мини-группе: от блокчейна до первой покупки, своего кошелька и криптовалютной карты.</p><span class="more">Программа курса</span><div class="big">{BTC}</div></a>
</div></div></section>

<section class="light">
<div class="wrap">
<div class="kicker fade">Запросы</div>
<h2 class="fade">С какими вопросами ко мне приходят</h2>
<p class="sub fade">Узнали свой вопрос? Приходите на бесплатную встречу, разберём его вместе.</p>
<div class="qs fade">{''.join(f'<div>{q}</div>' for q in qs)}</div>
</div></section>

<section class="light" id="services" style="padding-top:20px">

<div class="wrap">
<div class="kicker fade">Услуги и цены</div>
<h2 class="fade">Что можно у меня заказать</h2>
<p class="sub fade">Три направления: разовые консультации, долгосрочная работа и мои продукты.</p>
{svc_html}
</div></section>

<section class="club" id="club"><div class="wrap">
<div class="kicker fade">Сообщество</div>
<h2 class="fade">Финансовый клуб</h2>
<p class="sub fade">Закрытое сообщество для тех, кто хочет держать свои финансы в порядке постоянно, а не только во время практикума. Мы рядом, когда меняются законы, санкции и налоги, и когда нужно открыть новый счёт или выбрать инструмент.</p>
<div class="club-card fade">
<div class="club-side"><div class="t">Подписка</div><div class="cp">€33 <small>в месяц</small></div><div class="eur">≈ 3 900 дин. в месяц</div>
<p class="club-note">Клуб доступен для тех, кто прошёл практикум «Путь к финансовой свободе» или личные консультации по инвестициям. Оставить предварительную запись можно уже сейчас.</p>
<a class="btn" href="{PRACTICUM}#signup" target="_blank" rel="noopener">Предварительная запись в клуб</a>
<a class="more" href="club/">Подробнее о клубе →</a></div>
<div class="club-grid"><div class="ct"><b>Ответы на все вопросы</b><p>Постоянная помощь в закрытом чате от Анны и Екатерины: пишете вопрос — получаете ответ.</p></div><div class="ct"><b>Динамические модельные портфели</b><p>Модельные портфели от наших партнёров с 30-летним опытом инвестирования: регулярно обновляются и адаптированы под рынок. Плюс регулярные новости фондового рынка.</p></div><div class="ct"><b>Брокеры и брокерские счета</b><p>Актуальные инструкции и помощь: какого брокера выбрать, как открыть счёт и подключиться.</p></div><div class="ct"><b>Законы, налоги и санкции</b><p>Гайды и обновления по всем изменениям в России и Сербии, которые касаются нас, резидентов: налоги, санкции, как платить.</p></div><div class="ct"><b>Альтернативные инструменты</b><p>Актуальная информация об альтернативных инструментах для инвестирования.</p></div><div class="ct"><b>Криптовалюта</b><p>Как купить биткоин, пошаговые гайды и помощь в открытии криптобирж и криптокошельков.</p></div><div class="ct"><b>Переводы</b><p>Актуальная информация по валютным и денежным переводам и переводам в криптовалюте: рубли, SWIFT, криптовалюта — и ответы на вопросы, если нужно сделать перевод.</p></div><div class="ct"><b>Финансовые новости</b><p>Актуальные финансовые новости от наших партнёров — коротко и по делу.</p></div><div class="ct"><b>Онлайн-встречи каждый месяц</b><p>Разбираем актуальные темы вместе и отвечаем на вопросы вживую.</p></div><div class="ct"><b>Страхование</b><p>Ответы на все ваши вопросы о страховании семьи, здоровья и имущества.</p></div><div class="ct"><b>Бюджет и личные финансы</b><p>Помощь с настройкой своей финансовой системы и ведением бюджета.</p></div><div class="ct"><b>Бот-ассистент бесплатно</b><p>На всё время участия в клубе — бот, который голосом помогает вести бюджет за 5 минут в день.</p></div><div class="ct"><b>Скидка 30% на консультации</b><p>На все личные консультации с Анной и Екатериной.</p></div><div class="ct"><b>Шаблоны, гайды и инструкции</b><p>Всё доступно всем участникам клуба, с инструкциями, как этим пользоваться: шаблон бюджета, подбор страхования, расчёт пенсионного капитала, расчёт, сколько инвестировать под вашу цель, риск-профиль и шаблон личного финансового плана.</p></div></div>
</div>
</div></section>

<section class="light" style="padding-top:20px">
<div class="wrap">
<div class="kicker fade">Как записаться</div>
<h2 class="fade" style="margin-bottom:40px">Три простых шага</h2>
<div class="steps fade">
<div><h3>Напишите в Telegram</h3><p>Нажмите «Записаться» — откроется чат со мной.</p></div>
<div><h3>Выберем время</h3><p>Договоримся о бесплатной встрече-знакомстве на 30 минут онлайн.</p></div>
<div><h3>Подберём формат</h3><p>Обсудим ваш запрос и решим, какой формат вам подойдёт.</p></div>
</div></div></section>

'''

# ---------------- BOT ----------------
bot_curr = [('1', 'Основная валюта', 'Если вы называете просто сумму, без валюты, бот запишет её в основной валюте.'),
            ('2', 'Вторая валюта', 'В ней бот тоже пересчитывает весь бюджет. Обычно это евро или доллары.'),
            ('🌍', 'Любая валюта мира', 'Поехали в Турцию и платите лирами? Пишите в лирах, бот сам пересчитает в обе ваши валюты.')]
bot_feats = [('🎙', 'Голосом или текстом', 'Скажите или напишите «кофе 5 евро» или «молоко 120, яйца 150, сок 200». Бот сам поймёт статью, посчитает сумму и запишет. Ошиблись? Нажмите «Отменить».'),
             ('💱', 'Мультивалютность', 'Две ваши валюты: основная и вторая, обычно евро или доллары. Пишите в любой валюте мира, бот пересчитает каждую запись в обе.'),
             ('📊', 'Таблица и дашборды', 'Своя Google-таблица на вашем Диске: готовый дашборд, отчёты по статьям, бюджет план/факт и мини-урок. Данные лежат одним массивом, можно строить свои отчёты.'),
             ('👨‍👩‍👧', 'Семейный бюджет', 'Можно добавить несколько человек. Каждый пишет своему ассистенту, а всё попадает в одну общую таблицу.'),
             ('💼', 'Доходы и расходы бизнеса', 'Свои статьи бизнеса и план по месяцам тоже ведутся через бота. Видно, сколько бизнес приносит на самом деле.'),
             ('🎯', 'Цели и накопления', 'План по месяцам и главное — годовая цель. Каждый месяц видно, насколько вы приблизились или отстали и что поправить.')]
bot_body = f'''
<section class="hero phero">

<div class="wrap phero-grid">
<div>
<div class="eyebrow"><img src="bot-avatar.png" alt="">Telegram-бот · @BudgetAssistantPavlovaBot</div>
<h1 style="color:#fff;text-transform:uppercase;margin-bottom:22px">Бюджет-ассистент</h1>
<p class="lead">Записывайте траты голосом в любой валюте мира. Бот сам пересчитает их в две ваши валюты и занесёт в Google-таблицу с дашбордом.</p>
<div class="hero-btns"><a class="btn btn-blue" href="{BOT}" target="_blank" rel="noopener">{TGSVG}Открыть бота</a><a class="btn btn-ghost" href="#price">Стоимость</a></div>
</div>
<img class="shot" src="bot-screenshot.jpg" width="660" height="1431" alt="Бюджет-ассистент в Telegram: голосовое сообщение и запись трат в таблицу">
</div></section>

<section class="light">

<div class="wrap">
<div class="kicker fade">Валюты</div>
<h2 class="fade">Две ваши валюты, а записывать можно в любой</h2>
<p class="sub fade">При настройке вы выбираете две валюты, и бот всё время пересчитывает каждую запись в обе.</p>
<div class="grid g3">{''.join(f'<div class="card fade"><div class="ic" style="font-size:22px">{i}</div><h3>{h}</h3><p>{t}</p></div>' for i, h, t in bot_curr)}</div>
</div></section>

<section class="dark">

<div class="wrap">
<div class="kicker fade">Возможности</div>
<h2 class="fade">Учёт без потери времени</h2>
<p class="sub fade" style="margin-bottom:12px">Быстро, просто и сразу в нужной таблице: одно сообщение — и трата уже в вашем бюджете.</p>
<p class="sub fade">Учёт показывает, сколько реально остаётся на подушку и инвестиции. Без него мы просто надеемся, что «как-нибудь хватит».</p>
<div class="grid g3">{''.join(f'<div class="card fade"><div class="ic" style="font-size:22px">{i}</div><h3>{h}</h3><p>{t}</p></div>' for i, h, t in bot_feats)}</div>
</div></section>

<section class="light">

<div class="wrap">
<div class="kicker fade">Как начать</div>
<h2 class="fade" style="margin-bottom:40px">Три шага до порядка в деньгах</h2>
<div class="steps fade">
<div><h3>Откройте бота</h3><p>Перейдите в @BudgetAssistantPavlovaBot и нажмите «Старт».</p></div>
<div><h3>Получите таблицу</h3><p>Бот подключит вашу Google-таблицу с готовыми статьями и дашбордом.</p></div>
<div><h3>Пишите или говорите</h3><p>Каждая трата — одно сообщение. В конце месяца видна вся картина.</p></div>
</div></div></section>

<section class="dark" id="club">

<div class="wrap">
<div class="kicker fade">Финансовый клуб</div>
<h2 class="fade">Бот бесплатно в Финансовом клубе Анны и Екатерины</h2>
<p class="sub fade">Закрытое сообщество для тех, кто хочет держать свои финансы в порядке постоянно. Мы рядом, когда меняются законы, санкции и налоги, и когда нужно открыть новый счёт или выбрать инструмент.</p>
<div class="grid g3">
<div class="card fade"><div class="ic" style="font-size:22px">🤖</div><h3>Бот-ассистент бесплатно</h3><p>На всё время участия в клубе: ведите бюджет голосом за 5 минут в день.</p></div>
<div class="card fade"><div class="ic" style="font-size:22px">💬</div><h3>Ответы на вопросы</h3><p>Постоянная помощь в закрытом чате от Анны Чачиной и Екатерины Павловой.</p></div>
<div class="card fade"><div class="ic" style="font-size:22px">📁</div><h3>Шаблоны и скидка 30%</h3><p>Шаблон бюджета, личного финплана, расчёт пенсионного капитала и скидка 30% на личные консультации.</p></div>
</div>
<p class="note" style="color:rgba(255,255,255,.65)">Подписка €33 в месяц. Клуб доступен для тех, кто прошёл практикум «Путь к финансовой свободе» или личные консультации по инвестициям, предварительная запись уже идёт.</p>
<div class="hero-btns" style="margin:26px 0 0"><a class="btn btn-blue" href="../club/">Подробнее о клубе</a></div>
</div></section>

<section class="light" id="price">
<div class="wrap">
<div class="kicker fade">Стоимость</div>
<h2 class="fade">Подписка</h2>
<p class="sub fade">Первый месяц бесплатно — попробуйте и решите, подходит ли вам.</p>
<div class="prices p2">
<div class="price fade"><h3>Месяц</h3><div class="val">€9</div><div class="dur">в месяц</div><p>Бот, Google-таблица с дашбордом, мини-видеоурок и клуб «Финансовая база».</p><a class="btn btn-line" href="{BOT}" target="_blank" rel="noopener">Начать бесплатно</a></div>
<div class="price pop fade"><span class="lbl">Выгоднее</span><h3>Год</h3><div class="val">€90</div><div class="dur">за год · 2 месяца в подарок</div><p>Всё то же самое на весь год, без ежемесячных списаний.</p><a class="btn btn-blue" href="{BOT}" target="_blank" rel="noopener">Открыть бота</a></div>
</div>
<p class="note">В подписку входит клуб «Финансовая база»: еженедельные посты, ответы на вопросы и обратная связь по бюджету. Настройка бота и бюджета и другие услуги — на странице <a href="../#services">«Все услуги и цены»</a>.</p>
</div></section>
'''

# ---------------- CRYPTO ----------------
lessons = [
 ('Знакомство с криптовалютой', 'С чего всё началось и как это устроено',
  ['Что такое криптовалюта и с чего всё началось','Биткоин: как и кем он был создан и почему он главный','Циклы биткоина и халвинг','Блокчейн: как это работает','Какие функции у криптовалюты: сбережения, инвестиции, переводы, платежи','Децентрализованные монеты и токены, у которых есть эмитент','Капитализация и объём: сколько занимает криптовалюта на фоне фондового рынка и золота'],
  'Тест по уроку и определяем свой риск-профиль: криптовалюта — достаточно рискованный инструмент'),
 ('Безопасность', 'Самый важный урок: как не потерять деньги',
  ['Централизованные и децентрализованные биржи: какие риски и как выбрать биржу','Двухфакторная аутентификация и защита аккаунта','Какие бывают кошельки (горячие, холодные, некастодиальные)','Как правильно хранить сид-фразу','Что такое сети и почему их важно не перепутать','AML-проверка: почему криптовалюту и стейблкоины могут заблокировать и как проверить монеты, чтобы избежать блокировки','Как защититься от мошенников'],
  'Тест по уроку и открываем некастодиальный кошелёк (MetaMask или Rabby)'),
 ('Альткоины и стейблкоины', 'Подробно разбираем монеты и риски',
  ['Коины, токены, альткоины и стейблкоины: в чём разница','Биткоин и все остальные монеты: доля каждой на рынке','Почему весь рынок ходит за биткоином','Стейблкоины: чем отличается USDT от USDC и чем они обеспечены','Почему я не рекомендую инвестировать в альткоины: разбираем на примере SUI и проектов, которые были на хайпе в прошлом цикле','Почему многие монеты живут всего один цикл и угадать победителя почти невозможно','CoinMarketCap и CoinGecko: капитализация, объём, доминация и основные индикаторы','Индекс страха и жадности: как понять настроение рынка','Где брать новости и как отличать информацию от хайпа'],
  'Тест по уроку'),
 ('Налоги и законы', 'Чтобы всё было законно и спокойно',
  ['Закон о цифровых активах в Сербии','Как в Европе контролируют биржи и почему могут перестать обслуживать граждан и резидентов России','Как считаются и платятся налоги на криптовалюту в Сербии','Закон о цифровых активах в России','Новый закон о криптовалюте в РФ: что теперь можно'],
  'Тест по уроку и вместе начинаем регистрацию на бирже: верификация может занять несколько дней'),
 ('Как купить криптовалюту и переводить деньги', 'Покупка, продажа и переводы на практике',
  ['Проверяем, что аккаунт на бирже готов, и разбираемся в интерфейсе','Как купить и продать криптовалюту за фиатные деньги','Переводы внутри биржи','Ончейн-переводы через блокчейн: выбираем сеть, проверяем адрес и делаем перевод на свой кошелёк','Денежные переводы между странами через криптовалюту','Криптовалютные карты: как расплачиваться криптовалютой как обычной картой','Что можно купить за криптовалюту'],
  'Тест по уроку. Покупаем первую криптовалюту, делаем перевод и оформляем криптовалютную карту'),
 ('Виды заработка на криптовалюте', 'Какие стратегии существуют и что подходит вам',
  ['Долгосрочное инвестирование и регулярные покупки (DCA)','Что такое трейдинг и почему успешных трейдеров только 1%','Стейкинг и earn-продукты на биржах','DeFi: доходность без посредников и её риски','Торговые боты: что это такое и какие бывают','Как правильно подобрать стратегию с учётом вашего риск-профиля'],
  'Тест по уроку и подбираем стратегию под свой риск-профиль'),
]
les_html = ''.join(f'''<details class="lesson fade"{' open' if i == 0 else ''}><summary><span class="n">{i+1:02d}</span><h3>{t}<small>{s}</small></h3><span class="pl">+</span></summary>
<div class="body"><ul>{''.join(f'<li>{x}</li>' for x in items)}</ul><div class="prac"><b>Практика</b>{p}</div></div></details>''' for i, (t, s, items, p) in enumerate(lessons))

crypto_body = f'''
<section class="hero phero">

<div class="wrap phero-grid">
<div>
<div class="eyebrow"><i></i>Авторский курс · мини-группа до 5 человек</div>
<h1 style="color:#fff;text-transform:uppercase;margin-bottom:22px">Азы криптовалют</h1>
<p class="lead">От понимания, что такое блокчейн, до первой покупки и криптовалютной карты — вживую и под моим личным контролем</p>
<p style="display:inline-block;background:rgba(255,255,255,.08);border:1px solid rgba(117,230,254,.35);color:#fff;border-radius:12px;padding:10px 16px;margin:0 0 26px;font-weight:600">Чёрная пятница: <s style="opacity:.6">€500</s> €390 до 30 ноября</p>
<div class="hero-btns"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Записаться в группу</a><a class="btn btn-ghost" href="#program">Программа</a></div>
</div>
<div class="grid" style="gap:14px">
<div class="card ink" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><h3>6 живых уроков по 60 минут</h3><p>Два раза в неделю, без перегруза и без записей вместо занятий — всё вживую, с вопросами по ходу.</p></div>
<div class="card ink" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><h3>До 5 человек</h3><p>Мини-группа, чтобы я успевала разобрать ситуацию каждого.</p></div>
<div class="card ink" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><h3>Тест после каждого урока</h3><p>Закрепляем материал и сразу видим, что нужно повторить. Даю обратную связь.</p></div>
</div>
</div></section>

<section class="light">

<div class="wrap">
<div class="kicker fade">Для кого</div>
<h2 class="fade">Курс для вас, если</h2>
<div class="grid g4" style="margin-top:34px">
<div class="card fade"><div class="ic">1</div><p>Давно хотите разобраться в криптовалюте, но не знаете, с чего начать</p></div>
<div class="card fade"><div class="ic">2</div><p>Боитесь ошибиться с переводом или потерять деньги из-за мошенников</p></div>
<div class="card fade"><div class="ic">3</div><p>Хотите платить криптовалютой и переводить деньги между странами</p></div>
<div class="card fade"><div class="ic">4</div><p>Думаете об инвестициях в криптовалюту, но пока не решились</p></div>
</div></div></section>

<section class="light" id="program" style="padding-top:20px">
<div class="wrap">
<div class="kicker fade">Программа</div>
<h2 class="fade">Шесть уроков — от основ до первой покупки</h2>
<p class="sub fade">В каждом уроке теория и практика: по ходу курса вы шаг за шагом настраиваете всё, что нужно для жизни с криптовалютой.</p>
<div class="lessons">{les_html}</div>
</div></section>

<section class="dark">

<div class="wrap">
<div class="kicker fade">Результат</div>
<h2 class="fade">Что у вас будет после курса</h2>
<p class="sub fade">Не просто знания, а работающая инфраструктура — настроенная вами лично под моим контролем.</p>
<div class="results fade">
<div><i>⇄</i>Аккаунт на бирже</div><div><i>🔒</i>Свой кошелёк</div><div><i>💳</i>Криптовалютная карта</div><div><i>₿</i>Первая покупка</div><div><i>↗</i>Первый перевод</div>
</div>
<div class="pills" style="justify-content:center;margin-top:40px"><span class="pill">Все уроки вживую, 2 раза в неделю</span><span class="pill">Тест после каждого урока</span><span class="pill">Презентации к урокам остаются с вами навсегда</span><span class="pill">Криптословарь</span><span class="pill">Чат поддержки на весь курс: ответы на все вопросы</span><span class="pill">Ещё месяц поддержки после курса</span></div>
</div></section>

<section class="light">
<div class="wrap" style="max-width:820px">
<div class="price pop fade" style="padding:44px;text-align:center"><span class="lbl">Чёрная пятница · −22% · мини-группа до 5 человек</span>
<h3 style="font-size:28px;text-transform:uppercase">Курс «Азы криптовалют»</h3>
<div class="dur" style="margin:14px 0 0"><s>€500</s> · Чёрная пятница до 30 ноября</div><div class="val">€390</div><div class="dur">за весь курс · 6 живых уроков по 60 минут · 2 раза в неделю · тест после каждого урока · чат поддержки на весь курс и месяц после</div>
<p>Скидка Чёрной пятницы действует до 30 ноября, потом курс будет стоить €500. Напишите мне — расскажу о дате старта и забронирую место в группе.</p>
<a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener" style="width:auto;align-self:center">{TGSVG}Узнать дату старта</a></div>
<p class="note" style="text-align:center">Другие услуги — на странице <a href="../#services">«Все услуги и цены»</a>.</p>
</div></section>
'''


# ---------------- CLUB ----------------
club_feats = [('💬', 'Ответы на все вопросы', 'Постоянная помощь в закрытом чате от Анны и Екатерины: пишете вопрос — получаете ответ.'),
 ('📈', 'Модельные портфели', 'Динамические портфели от наших партнёров с 30-летним опытом инвестирования, регулярно обновляются. Плюс новости фондового рынка.'),
 ('🏦', 'Брокеры и счета', 'Какого брокера выбрать, как открыть счёт и подключиться: актуальные инструкции и помощь.'),
 ('⚖️', 'Законы, налоги и санкции', 'Гайды и обновления по всем изменениям в России и Сербии, которые касаются нас: налоги, санкции, как платить.'),
 ('🧩', 'Альтернативные инструменты', 'Актуальная информация об альтернативных инструментах для инвестирования.'),
 ('🪙', 'Криптовалюта', 'Как купить биткоин, пошаговые гайды и помощь с криптобиржами и кошельками.'),
 ('🌍', 'Переводы', 'Рубли, SWIFT, криптовалюта: как сделать перевод сейчас и ответы на вопросы, если нужно перевести деньги.'),
 ('📰', 'Финансовые новости', 'Новости от наших партнёров — коротко и по делу.'),
 ('🎥', 'Онлайн-встречи каждый месяц', 'Разбираем актуальные темы вместе и отвечаем на вопросы вживую.'),
 ('🛡', 'Страхование', 'Ответы на вопросы о страховании семьи, здоровья и имущества.'),
 ('📊', 'Бюджет и личные финансы', 'Помощь с настройкой своей финансовой системы и ведением бюджета.'),
 ('🤖', 'Бот-ассистент бесплатно', 'На всё время участия в клубе — бот, который голосом помогает вести бюджет за 5 минут в день.'),
 ('💸', 'Скидка 30% на консультации', 'На все личные консультации с Анной и Екатериной.'),
 ('📁', 'Шаблоны и гайды', 'Шаблон бюджета, подбор страхования, расчёт пенсионного капитала, риск-профиль и шаблон личного финплана — с инструкциями.'),
 ('🤝', 'Свои люди рядом', 'Сообщество русскоязычных резидентов, которые тоже наводят порядок в деньгах.')]
club_body = f'''
<section class="hero phero">

<div class="wrap phero-grid">
<div>
<div class="eyebrow"><i></i>Закрытое сообщество · Анна Чачина и Екатерина Павлова</div>
<h1 style="color:#fff;text-transform:uppercase;margin-bottom:22px">Финансовый клуб</h1>
<p class="lead">Для тех, кто хочет держать свои финансы в порядке постоянно. Мы рядом, когда меняются законы, санкции и налоги, и когда нужно открыть новый счёт или выбрать инструмент.</p>
<div class="hero-btns"><a class="btn btn-blue" href="{PRACTICUM}#signup" target="_blank" rel="noopener">Предварительная запись</a><a class="btn btn-ghost" href="#price">Стоимость</a></div>
</div>
<div class="price pop" style="color:var(--text);text-align:center;max-width:340px;justify-self:center;width:100%"><span class="lbl">Подписка</span>
<h3>Финансовый клуб</h3><div class="val">€33</div><div class="dur">в месяц</div><p>Чат с ответами, встречи каждый месяц, шаблоны, бот бесплатно и скидка 30% на консультации.</p>
<a class="btn btn-blue" href="{PRACTICUM}#signup" target="_blank" rel="noopener">Оставить заявку</a></div>
</div></section>

<section class="light">
<div class="wrap">
<div class="kicker fade">Что внутри</div>
<h2 class="fade">Всё, что нужно, в одном месте</h2>
<p class="sub fade">Не нужно искать ответы по разным чатам и каналам: спрашиваете — мы отвечаем и держим в курсе.</p>
<div class="grid g3">{''.join(f'<div class="card fade"><div class="ic" style="font-size:22px">{i}</div><h3>{h}</h3><p>{t}</p></div>' for i, h, t in club_feats)}</div>
</div></section>

<section class="dark" id="price">
<div class="wrap" style="max-width:820px;text-align:center">
<div class="kicker fade" style="justify-content:center">Как вступить</div>
<h2 class="fade" style="margin:0 auto 14px">€33 в месяц</h2>
<p class="sub fade" style="margin:0 auto 30px">Клуб доступен для тех, кто прошёл практикум «Путь к финансовой свободе» или личные консультации по инвестициям. Оставить предварительную запись можно уже сейчас.</p>
<div class="hero-btns" style="justify-content:center;margin:0"><a class="btn btn-blue" href="{PRACTICUM}#signup" target="_blank" rel="noopener">Предварительная запись</a><a class="btn btn-ghost" href="{PRACTICUM}" target="_blank" rel="noopener">О практикуме</a></div>
</div></section>
'''

os.makedirs('bot', exist_ok=True)
os.makedirs('club', exist_ok=True)
os.makedirs('crypto', exist_ok=True)
pages = {
 'index.html': page('Екатерина Павлова — международный финансовый советник', 'Екатерина Павлова, международный финансовый советник. Личные финансы, криптовалюта, налоги, инвестиции. Бесплатная встреча-знакомство 30 минут.', 'index', '', main_body),
 'bot/index.html': page('Бюджет-ассистент — Telegram-бот для учёта финансов | Екатерина Павлова', 'Telegram-бот для учёта личных финансов и мини-бизнеса: голосовой ввод, несколько валют, Google-таблица с дашбордом. Первый месяц бесплатно.', 'bot', '../', bot_body),
 'crypto/index.html': page('Курс «Азы криптовалют» — мини-группа до 5 человек | Екатерина Павлова', 'Авторский курс Екатерины Павловой: блокчейн, биткоин, безопасность, стейблкоины, налоги. Живые уроки, тест после каждого урока, поддержка в чате, первая покупка и свой кошелёк.', 'crypto', '../', crypto_body),
 'club/index.html': page('Финансовый клуб Анны Чачиной и Екатерины Павловой', 'Закрытое сообщество для русскоязычных резидентов Сербии: ответы на вопросы, модельные портфели, налоги и санкции, встречи каждый месяц, бот-ассистент бесплатно. €33 в месяц.', 'club', '../', club_body),
}
for path, html in pages.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('ok', path, len(html))

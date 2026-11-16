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

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=PT+Serif:ital,wght@0,700;1,400&display=swap" rel="stylesheet">'

CSS = r"""
:root{--ink:#141a47;--ink-2:#1e2761;--ink-3:#2a3478;--blue:#2554d6;--blue-2:#3a6cf0;--cyan:#75e6fe;
--bg:#f4f6fc;--card:#fff;--line:#e2e5f0;--text:#1d2340;--muted:#5d647f}
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
.btn-blue{background:var(--blue);color:#fff;box-shadow:0 12px 30px -10px rgba(37,84,214,.75)}
.btn-blue:hover{background:var(--blue-2);transform:translateY(-2px)}
.btn-ghost{color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.35)}
.btn-ghost:hover{box-shadow:inset 0 0 0 1px #fff;background:rgba(255,255,255,.06)}
.btn-line{color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--ink)}.btn-line:hover{background:var(--ink);color:#fff}

/* header */
header{position:fixed;inset:0 0 auto;z-index:50;background:rgba(20,26,71,.9);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.08)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:20px;color:#fff}
.brand{text-decoration:none;line-height:1.2;display:flex;align-items:center;gap:12px}
.brand .mark{width:38px;height:38px;border-radius:10px;background:var(--blue);display:grid;place-items:center;font-family:"PT Serif",serif;font-weight:700;font-size:17px}
.brand b{font-family:"PT Serif",serif;font-size:18px;display:block}
.brand span{font-size:12.5px;color:rgba(255,255,255,.6)}
.nav ul{display:flex;gap:26px;list-style:none;font-size:15px}
.nav ul a{text-decoration:none;color:rgba(255,255,255,.72);transition:color .2s;padding:6px 0;border-bottom:2px solid transparent}
.nav ul a:hover{color:#fff}.nav ul a.on{color:#fff;border-color:var(--cyan)}
.nav .btn{padding:11px 18px;font-size:15px}
.burger{display:none;background:none;border:0;color:#fff;width:40px;height:40px;cursor:pointer}
.burger svg{width:26px;height:26px}
@media(max-width:960px){.nav ul{display:none;position:absolute;top:72px;left:0;right:0;flex-direction:column;gap:0;background:var(--ink);padding:10px 24px 20px;border-bottom:1px solid rgba(255,255,255,.1)}
.nav ul.open{display:flex}.nav ul a{display:block;padding:12px 0}.burger{display:block}}
@media(max-width:520px){.nav .btn{display:none}.brand span{display:none}}

/* bitcoin background */
.btc-bg{position:absolute;pointer-events:none;color:#fff;opacity:.05;z-index:0;animation:float 14s ease-in-out infinite}
.btc-bg svg{width:100%;height:100%}
.light .btc-bg{color:var(--ink);opacity:.035}
@keyframes float{0%,100%{transform:translateY(0) rotate(-8deg)}50%{transform:translateY(-28px) rotate(6deg)}}
@keyframes spin{to{transform:rotate(360deg)}}
canvas.net{position:absolute;inset:0;width:100%;height:100%;z-index:0;opacity:.55}

/* hero */
.hero{background:radial-gradient(900px 520px at 85% 0%,rgba(37,84,214,.45),transparent 60%),radial-gradient(700px 500px at 0% 100%,rgba(117,230,254,.12),transparent 60%),var(--ink);color:#fff;padding:150px 0 0;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.25fr .75fr;gap:40px;align-items:end;position:relative;z-index:1}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:14px;color:var(--cyan);border:1px solid rgba(117,230,254,.3);padding:8px 16px;border-radius:999px;margin-bottom:26px}
.eyebrow i{width:8px;height:8px;border-radius:50%;background:var(--cyan);box-shadow:0 0 0 4px rgba(117,230,254,.2);animation:pulse 2s infinite}
@keyframes pulse{50%{box-shadow:0 0 0 8px rgba(117,230,254,0)}}
.hero h1{color:#fff;font-size:clamp(36px,5.4vw,64px);text-transform:uppercase;max-width:15ch;margin-bottom:22px}
.hero .lead{font-family:"PT Serif",serif;font-style:italic;font-size:clamp(19px,2vw,23px);color:rgba(255,255,255,.85);max-width:34ch;margin-bottom:36px}
.hero-btns{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:56px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid rgba(255,255,255,.14);padding:26px 0 40px;gap:20px}
.stats b{font-family:"PT Serif",serif;font-size:36px;color:var(--cyan);display:block;line-height:1.1}
.stats span{font-size:14px;line-height:1.4;display:block;color:rgba(255,255,255,.65)}
.photo{position:relative;align-self:end;justify-self:center;width:100%;max-width:380px}
.photo::before{content:"";position:absolute;inset:-18px -18px auto auto;width:70%;height:70%;border:1.5px solid rgba(117,230,254,.45);border-radius:20px}
.photo img{position:relative;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;border-radius:20px 20px 0 0;box-shadow:0 30px 70px -20px rgba(0,0,0,.6)}
.photo .badge{position:absolute;left:-26px;bottom:40px;background:#fff;color:var(--ink);border-radius:14px;padding:12px 16px;display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600;box-shadow:0 18px 40px -12px rgba(0,0,0,.5);animation:float2 6s ease-in-out infinite}
.photo .badge svg{width:30px;height:30px;color:#f7931a}
@keyframes float2{50%{transform:translateY(-10px)}}
@media(max-width:860px){.hero-grid{grid-template-columns:1fr}.photo{max-width:320px}.stats{grid-template-columns:1fr 1fr 1fr}.stats b{font-size:28px}}

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
.card:hover{transform:translateY(-4px);box-shadow:0 24px 50px -24px rgba(20,26,71,.35)}
.card h3{margin-bottom:8px}
.card p{color:var(--muted);font-size:16px}
.card .ic{width:46px;height:46px;border-radius:12px;background:rgba(37,84,214,.1);color:var(--blue);display:grid;place-items:center;margin-bottom:18px;font-weight:700;font-family:"PT Serif",serif;font-size:18px}
.card .ic svg{width:24px;height:24px}
.card.ink{background:var(--ink-2);border-color:var(--ink-2);color:#fff}.card.ink h3{color:#fff}.card.ink p{color:rgba(255,255,255,.72)}
.dark .card{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1)}
.dark .card p{color:rgba(255,255,255,.7)}.dark .card .ic{background:rgba(117,230,254,.12);color:var(--cyan)}

/* about */
.about{display:grid;grid-template-columns:.8fr 1.2fr;gap:56px;align-items:start}
.about img{border-radius:20px;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.about ul{list-style:none;display:grid;gap:14px;margin-top:8px}
.about li{display:flex;gap:14px;font-size:17px}
.about li svg{flex:none;width:22px;height:22px;color:var(--blue);margin-top:2px}
@media(max-width:860px){.about{grid-template-columns:1fr}.about img{display:none}.photo .badge{left:-8px}}

/* services teaser */
.feat{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
@media(max-width:760px){.feat{grid-template-columns:1fr}}
.feat a{display:block;text-decoration:none;border-radius:22px;padding:36px;position:relative;overflow:hidden;min-height:300px;transition:transform .3s}
.feat a:hover{transform:translateY(-5px)}
.feat .f1{background:linear-gradient(140deg,var(--ink-2),var(--ink));color:#fff}
.feat .f2{background:linear-gradient(140deg,var(--blue),#1a3ea8);color:#fff}
.feat h3{color:#fff;font-size:26px;text-transform:uppercase;margin:14px 0 10px;max-width:16ch}
.feat p{color:rgba(255,255,255,.78);max-width:36ch;margin-bottom:22px}
.feat .tag{display:inline-block;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--cyan)}
.feat .f2 .tag{color:#fff;opacity:.85}
.feat .more{font-weight:600;display:inline-flex;gap:8px;align-items:center}
.feat .more::after{content:"→";transition:transform .25s}.feat a:hover .more::after{transform:translateX(5px)}
.feat .big{position:absolute;right:-30px;bottom:-40px;width:220px;height:220px;opacity:.1;color:#fff}
.feat .big svg{width:100%;height:100%}
.feat a:hover .big{animation:spin 12s linear infinite}

/* questions */
.qs{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.qs div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px 18px 50px;position:relative;font-size:16.5px}
.qs div::before{content:"?";position:absolute;left:16px;top:16px;width:24px;height:24px;border-radius:50%;background:var(--blue);color:#fff;font-size:14px;font-weight:700;display:grid;place-items:center}
@media(max-width:760px){.qs{grid-template-columns:1fr}}

/* prices */
.prices{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-bottom:22px}
@media(max-width:900px){.prices{grid-template-columns:1fr}}
.price{background:#fff;border:1px solid var(--line);border-radius:18px;padding:30px;display:flex;flex-direction:column;position:relative}
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
.plan .tag{display:inline-block;align-self:flex-start;font-size:12.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--cyan);border:1px solid rgba(117,230,254,.4);border-radius:999px;padding:5px 12px;margin-bottom:14px}
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
.results div i{display:grid;place-items:center;width:52px;height:52px;margin:0 auto 12px;border-radius:50%;background:rgba(117,230,254,.12);color:var(--cyan);font-style:normal;font-size:22px}

/* mock phone (bot) */
.phone{background:#0e1338;border-radius:34px;padding:14px;max-width:330px;margin:0 auto;box-shadow:0 40px 80px -30px rgba(0,0,0,.7),inset 0 0 0 1px rgba(255,255,255,.1);position:relative;z-index:1}
.chat{background:linear-gradient(#1b2357,#151c4a);border-radius:24px;padding:18px 14px;display:grid;gap:10px;min-height:420px;align-content:end}
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
.cta h2{margin:0 auto 14px;max-width:22ch}.cta .sub{margin:0 auto 34px}
.cta .hero-btns{justify-content:center;margin:0}
.note{font-size:14.5px;color:var(--muted);margin-top:18px}
.pill{display:inline-flex;align-items:center;gap:8px;background:rgba(37,84,214,.1);color:var(--blue);font-weight:600;font-size:14px;padding:7px 14px;border-radius:999px}
.dark .pill{background:rgba(117,230,254,.12);color:var(--cyan)}
.pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
footer{background:#0e1338;color:rgba(255,255,255,.6);padding:40px 0;font-size:14.5px}
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
// animated blockchain network
document.querySelectorAll('canvas.net').forEach(function(c){
  var x=c.getContext('2d'),P=[],W,H,dpr=Math.min(window.devicePixelRatio||1,2);
  function rs(){W=c.offsetWidth;H=c.offsetHeight;c.width=W*dpr;c.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);
    P=[];var n=Math.round(W*H/22000);for(var i=0;i<n;i++)P.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25})}
  rs();window.addEventListener('resize',rs);
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  (function f(){x.clearRect(0,0,W,H);
    for(var i=0;i<P.length;i++){var p=P[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;
      for(var j=i+1;j<P.length;j++){var q=P[j],d=Math.hypot(p.x-q.x,p.y-q.y);if(d<130){x.strokeStyle='rgba(117,230,254,'+(.18*(1-d/130))+')';x.lineWidth=1;x.beginPath();x.moveTo(p.x,p.y);x.lineTo(q.x,q.y);x.stroke()}}
      x.fillStyle='rgba(117,230,254,.5)';x.fillRect(p.x-1.5,p.y-1.5,3,3)}
    requestAnimationFrame(f)})();
});
})();
</script>
"""

def btc_bg(size, top, side, val, delay=0, extra=''):
    return f'<div class="btc-bg" style="width:{size}px;height:{size}px;top:{top};{side}:{val};animation-delay:-{delay}s{extra}">{BTC}</div>'

def header(active, root):
    items = [('index', 'Главная', root), ('about', 'Обо мне', root + '#about'), ('services', 'Услуги', root + '#services'),
             ('bot', 'Бюджет-ассистент', root + 'bot/'), ('crypto', 'Курс «Азы криптовалют»', root + 'crypto/'), ('contacts', 'Контакты', '#contacts')]
    lis = ''.join(f'<li><a href="{h}"{" class=on" if k == active else ""}>{t}</a></li>' for k, t, h in items if k != 'index')
    return f'''<header><div class="wrap nav">
<a class="brand" href="{root}"><span class="mark">ЕП</span><span><b>Екатерина Павлова</b><span>Финансовый советник · Сербия</span></span></a>
<ul>{lis}</ul>
<div style="display:flex;gap:10px;align-items:center"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Записаться</a>
<button class="burger" aria-label="Меню"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div>
</div></header>'''

def footer():
    return f'''<section class="dark cta" id="contacts">
<canvas class="net"></canvas>{btc_bg(380,'10%','left','-90px',3)}{btc_bg(240,'45%','right','-40px',8)}
<div class="wrap fade">
<div class="kicker" style="justify-content:center">Контакты</div>
<h2>Начните с бесплатной встречи-знакомства</h2>
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
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://pavlova.fin-academy.net/ekaterina.jpg">
<meta name="theme-color" content="#141a47">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{header(active, root)}
{body}
{footer()}
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
       'Сооснователь клуба «Денежный поток»',
       'Работаю с клиентами по всему миру, помогаю создавать пассивный доход и достигать финансовых целей',
       'Инвестор, мама двоих подростков']

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

formats = [('Встреча-знакомство', 'Бесплатно', '30 минут', 'Обсудим ваш запрос и подберём формат взаимодействия', True),
           ('Консультация', '€150', '60 минут', 'Ответ на ваш конкретный вопрос', False),
           ('Аудит финансового состояния', '€150', '90 минут', 'Взгляд со стороны и письменные рекомендации', False)]
fcards = ''.join(f'''<div class="price{' pop' if p else ''} fade">{'<span class="lbl">Начните здесь</span>' if p else ''}
<h3>{n}</h3><div class="val">{v}</div><div class="dur">{d}</div><p>{t}</p>
<a class="btn {'btn-blue' if p else 'btn-line'}" href="{TG}" target="_blank" rel="noopener">Записаться</a></div>''' for n, v, d, t, p in formats)

main_body = f'''
<section class="hero">
<canvas class="net"></canvas>
{btc_bg(520,'8%','right','-120px')}{btc_bg(170,'62%','left','4%',6)}{btc_bg(90,'22%','left','46%',10)}
<div class="wrap hero-grid">
<div>
<div class="eyebrow"><i></i>Международный финансовый советник · Сербия</div>
<h1>Капитал, который работает на вас</h1>
<p class="lead">Помогаю навести порядок в деньгах, создать пассивный доход и спокойно войти в мир криптовалют — в любой стране мира</p>
<div class="hero-btns"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Бесплатная встреча 30 минут</a><a class="btn btn-ghost" href="crypto/">Курс «Азы криптовалют»</a></div>
<div class="stats"><div><b>25+</b><span>лет в корпоративных финансах</span></div><div><b>50+</b><span>клиентов по личным финансам</span></div><div><b>€0</b><span>первая встреча</span></div></div>
</div>
<div class="photo"><img src="ekaterina.jpg" alt="Екатерина Павлова"><div class="badge">{BTC}Эксперт по криптовалютам</div></div>
</div></section>

<section class="light" id="about">
{btc_bg(300,'12%','right','-80px',4)}
<div class="wrap about">
<img class="fade" src="ekaterina.jpg" alt="Екатерина Павлова" loading="lazy">
<div class="fade">
<div class="kicker">О себе</div>
<h2>Екатерина Павлова</h2>
<p class="sub" style="margin-bottom:22px">Международный финансовый советник, инвестор, игропрактик</p>
<ul>{li(bio)}</ul>
<div class="pills"><span class="pill">Личные финансы</span><span class="pill">Криптовалюта</span><span class="pill">Налоги в Сербии</span><span class="pill">Страхование</span><span class="pill">Инвестиции</span></div>
</div></div></section>

<section class="dark">
<canvas class="net"></canvas>{btc_bg(360,'20%','left','-100px',2)}
<div class="wrap">
<div class="kicker fade">Мои продукты</div>
<h2 class="fade">Инструменты, которые я сделала для вас</h2>
<p class="sub fade">Учёт и криптовалюта — две вещи, с которых чаще всего начинается порядок в деньгах. Для каждой у меня есть своё решение.</p>
<div class="feat">
<a class="f1 fade" href="bot/"><span class="tag">Telegram-бот</span><h3>Бюджет-ассистент</h3><p>Записываете расходы голосом, а бот сам раскладывает их по статьям в Google-таблицу в нужных валютах.</p><span class="more">Подробнее о боте</span><div class="big"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="26" fill="none" stroke="currentColor" stroke-width="3"/><path d="M32 14v18l12 8" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg></div></a>
<a class="f2 fade" href="crypto/"><span class="tag">Авторский курс · до 5 человек</span><h3>Азы криптовалют</h3><p>Живые уроки в мини-группе: от блокчейна до первой покупки, холодного кошелька и крипто-карты.</p><span class="more">Программа курса</span><div class="big">{BTC}</div></a>
</div></div></section>

<section class="light">
<div class="wrap">
<div class="kicker fade">Запросы</div>
<h2 class="fade">С какими вопросами ко мне приходят</h2>
<p class="sub fade">Узнали свой вопрос? Приходите на бесплатную встречу, разберём его вместе.</p>
<div class="qs fade">{''.join(f'<div>{q}</div>' for q in qs)}</div>
</div></section>

<section class="light" id="services" style="padding-top:20px">
{btc_bg(260,'40%','left','-90px',5)}
<div class="wrap">
<div class="kicker fade">Услуги и стоимость</div>
<h2 class="fade">Форматы консультаций</h2>
<p class="sub fade">Разовые встречи — когда нужен ответ на конкретный вопрос или взгляд со стороны.</p>
<div class="prices">{fcards}</div>
<h2 class="fade" style="margin-top:70px">Сопровождение по финансам</h2>
<p class="sub fade">Когда нужен не один ответ, а система: стратегия, план и поддержка во внедрении.</p>
<div class="plans">
<div class="plan fade"><h3>Стратегическая сессия</h3><div class="val">€500</div><div class="dur">2 встречи</div>
<ul>{li(['Разбор вашей финансовой ситуации','Личная индивидуальная стратегия'])}</ul>
<a class="btn btn-line" href="{TG}" target="_blank" rel="noopener">Записаться</a></div>
<div class="plan ink fade"><span class="tag">Максимум результата</span><h3>Финансовый план</h3><div class="val">от €1 500</div><div class="dur">5 встреч за 2 месяца</div>
<ul>{li(['Полный финансовый план','Изучение инструментов','Финансовая стратегия для достижения ваших целей','Подбор страховых и инвестиционных решений','Инструкции по открытию счетов','Менторская поддержка во внедрении стратегии'])}</ul>
<a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">Записаться</a></div>
</div>
<div class="grid g2" style="margin-top:22px">
<a class="card fade" href="crypto/" style="text-decoration:none"><div class="ic">{BTC}</div><h3>Курс «Азы криптовалют»</h3><p>€390 · мини-группа до 5 человек, живые уроки и личная проверка домашних заданий. Программа →</p></a>
<a class="card fade" href="bot/" style="text-decoration:none"><div class="ic">₽€</div><h3>Консультация по бюджету + настройка бота · €100</h3><p>Разбираем ваш бюджет и настраиваем бюджет-ассистента под вашу семью или бизнес →</p></a>
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

<section class="light" style="padding-top:20px">
<div class="wrap"><div class="card ink fade" style="padding:44px;display:grid;grid-template-columns:1.4fr .6fr;gap:30px;align-items:center">
<div><div class="kicker" style="color:var(--cyan)">Обучение</div><h3 style="font-size:28px;text-transform:uppercase;margin-bottom:12px">Практикум «Путь к финансовой свободе»</h3>
<p>Вместе с Анной Чачиной мы ведём русскоязычный практикум по личным финансам и инвестициям для резидентов Сербии: 6 модулей, в каждом практика.</p></div>
<a class="btn btn-blue" href="{PRACTICUM}" target="_blank" rel="noopener">Подробнее о практикуме</a>
</div></div></section>
'''

# ---------------- BOT ----------------
bot_feats = [('🎙', 'Голосом или текстом', 'Скажите «кофе 350 динаров» — бот поймёт сумму, валюту и статью и запишет сам.'),
             ('💱', 'Несколько валют', 'Динары, евро, рубли, доллары: бот пересчитывает в две ваши базовые валюты и сохраняет курс.'),
             ('📊', 'Своя Google-таблица', 'Все записи падают в вашу таблицу с готовым дашбордом: весь год на одном экране.'),
             ('👨‍👩‍👧', 'Ведём вместе', 'Каждый член семьи пишет ассистенту, а в таблице видно, кто внёс запись.'),
             ('💼', 'Бизнес отдельным блоком', 'Свои статьи доходов и расходов бизнеса, план и факт по месяцам — не смешиваем с семейными деньгами.'),
             ('🎯', 'Цели и накопления', 'Норма сбережений за год, сравнение с планом по целям и топ статей расходов.')]
bot_body = f'''
<section class="hero phero">
<canvas class="net"></canvas>{btc_bg(420,'10%','right','-100px')}{btc_bg(140,'70%','left','6%',7)}
<div class="wrap phero-grid">
<div>
<div class="eyebrow"><i></i>Telegram-бот · @BudgetAssistantPavlovaBot</div>
<h1 style="color:#fff;text-transform:uppercase;margin-bottom:22px">Бюджет-ассистент</h1>
<p class="lead">Помощник по учёту личных финансов, который подойдёт и для мини-бизнеса. Нельзя управлять тем, что не измеряешь.</p>
<div class="hero-btns"><a class="btn btn-blue" href="{BOT}" target="_blank" rel="noopener">{TGSVG}Открыть бота</a><a class="btn btn-ghost" href="#price">Стоимость</a></div>
</div>
<div class="phone"><div class="chat">
<div class="top"><i>₽€</i><div>Бюджет с Павловой<small>бот</small></div></div>
<div class="msg me voice" style="animation-delay:.4s">▶ <span><i style="height:8px"></i><i style="height:14px;animation-delay:.1s"></i><i style="height:10px;animation-delay:.2s"></i><i style="height:16px;animation-delay:.3s"></i><i style="height:9px;animation-delay:.4s"></i><i style="height:13px;animation-delay:.5s"></i><i style="height:7px;animation-delay:.6s"></i></span> 0:04</div>
<div class="msg bot" style="animation-delay:1.3s">✅ Записал: <b>Продукты</b><br>2 400 RSD = 20,5 € · 2 050 ₽<br><small style="opacity:.6">курс на сегодня</small></div>
<div class="msg me" style="animation-delay:2.3s">такси 15 евро</div>
<div class="msg bot" style="animation-delay:3.1s">✅ <b>Транспорт</b> · 15 €<br>За ноябрь потрачено 64% бюджета</div>
</div></div>
</div></section>

<section class="light">
{btc_bg(280,'20%','left','-90px',3)}
<div class="wrap">
<div class="kicker fade">Возможности</div>
<h2 class="fade">Учёт без таблиц и формул</h2>
<p class="sub fade">Учёт показывает, сколько реально остаётся на подушку и инвестиции. Без него мы просто надеемся, что «как-нибудь хватит».</p>
<div class="grid g3">{''.join(f'<div class="card fade"><div class="ic" style="font-size:22px">{i}</div><h3>{h}</h3><p>{t}</p></div>' for i, h, t in bot_feats)}</div>
</div></section>

<section class="dark">
<canvas class="net"></canvas>
<div class="wrap">
<div class="kicker fade">Как начать</div>
<h2 class="fade" style="margin-bottom:40px">Три шага до порядка в деньгах</h2>
<div class="steps fade">
<div><h3>Откройте бота</h3><p>Перейдите в @BudgetAssistantPavlovaBot и нажмите «Старт».</p></div>
<div><h3>Получите таблицу</h3><p>Бот подключит вашу Google-таблицу с готовыми статьями и дашбордом.</p></div>
<div><h3>Пишите или говорите</h3><p>Каждая трата — одно сообщение. В конце месяца видна вся картина.</p></div>
</div></div></section>

<section class="light" id="price">
<div class="wrap">
<div class="kicker fade">Стоимость</div>
<h2 class="fade">Подписка и настройка</h2>
<p class="sub fade">Первый месяц бесплатно — попробуйте и решите, подходит ли вам.</p>
<div class="prices">
<div class="price fade"><h3>Месяц</h3><div class="val">490 ₽</div><div class="dur">или 900 ⭐ Telegram Stars</div><p>Бот, Google-таблица с дашбордом, мини-видеоурок и клуб «Финансовая база».</p><a class="btn btn-line" href="{BOT}" target="_blank" rel="noopener">Начать бесплатно</a></div>
<div class="price pop fade"><span class="lbl">Выгоднее</span><h3>Год</h3><div class="val">9 000 ⭐</div><div class="dur">Telegram Stars · 2 месяца в подарок</div><p>Всё то же самое на весь год, без ежемесячных списаний.</p><a class="btn btn-blue" href="{BOT}" target="_blank" rel="noopener">Открыть бота</a></div>
<div class="price fade"><h3>Консультация + настройка</h3><div class="val">€100</div><div class="dur">личная встреча</div><p>Разберём ваш бюджет, настроим статьи, валюты и семейный доступ под вас.</p><a class="btn btn-line" href="{TG}" target="_blank" rel="noopener">Записаться</a></div>
</div>
<p class="note">В подписку входит клуб «Финансовая база»: еженедельные посты, ответы на вопросы и обратная связь по бюджету.</p>
</div></section>
'''

# ---------------- CRYPTO ----------------
lessons = [
 ('Знакомство с криптовалютой', 'Что это такое и почему это работает без банков',
  ['Что такое криптовалюта и криптография','Блокчейн: цепочка блоков, которую нельзя подделать','Биткоин — первая криптовалюта: лимит 21 млн, халвинг, Сатоши Накамото','Что такое сети: Bitcoin, Ethereum, TRON, BNB Chain, Solana и почему важно не перепутать сеть при переводе','Децентрализация и главные плюсы криптовалюты','Публичный и приватный ключ: что подтверждает, что актив ваш'],
  'Регистрируемся на криптобирже и проходим верификацию'),
 ('Безопасность', 'Как не потерять деньги и не попасться мошенникам',
  ['Как хранить ключи и сид-фразу','Горячие и холодные кошельки: в чём разница','Популярные схемы мошенников и как от них защититься','Централизованные (CEX) и децентрализованные (DEX) биржи','Двухфакторная защита и «гигиена» аккаунтов'],
  'Открываем холодный кошелёк и правильно сохраняем сид-фразу'),
 ('Альткоины и стейблкоины', 'Какие бывают монеты и в чём их риски',
  ['Что такое альткоины и секторы рынка: DeFi, RWA, NFT, L1/L2, мем-коины','Стейблкоины: зачем нужны и кто их выпускает','Чем отличается USDT от USDC','Почему стейблкоины вроде USDC можно заблокировать — даже в холодном кошельке','Почему биткоин задаёт направление всему рынку'],
  'Делаем первую покупку и перевод криптовалюты на свой кошелёк'),
 ('Информационные ресурсы и циклы рынка', 'Где брать данные и как понимать, что происходит',
  ['Знакомимся с CoinMarketCap и CoinGecko','Капитализация, объём, доминация биткоина: как читать цифры','Циклы биткоина и халвинг','Где брать новости и как отличать информацию от хайпа'],
  'Собираем свой список отслеживаемых монет'),
 ('Виды заработка на криптовалюте', 'Какие стратегии существуют и что подходит вам',
  ['Долгосрочное инвестирование и регулярные покупки (DCA)','Трейдинг: что это и почему это не для всех','Стейкинг и earn-продукты на биржах','DeFi: доходность без посредников и её риски','Крипто-карты: как расплачиваться криптой как обычной картой'],
  'Оформляем крипто-карту'),
 ('Налоги', 'Как всё сделать законно',
  ['Налог на криптовалюту в Сербии: 15% на прирост капитала и льгота 90 дней','Почему важно сохранять подтверждение цены покупки','Новый закон о криптовалюте в РФ (282-ФЗ): что важно резидентам и нерезидентам','Налоговое резидентство: где и что платить','Как вести учёт сделок'],
  'Настраиваем учёт своих операций'),
]
les_html = ''.join(f'''<details class="lesson fade"{' open' if i == 0 else ''}><summary><span class="n">{i+1:02d}</span><h3>{t}<small>{s}</small></h3><span class="pl">+</span></summary>
<div class="body"><ul>{''.join(f'<li>{x}</li>' for x in items)}</ul><div class="prac"><b>Практика</b>{p}</div></div></details>''' for i, (t, s, items, p) in enumerate(lessons))

crypto_body = f'''
<section class="hero phero">
<canvas class="net"></canvas>{btc_bg(560,'4%','right','-140px')}{btc_bg(150,'68%','left','5%',6)}{btc_bg(80,'18%','left','52%',11)}
<div class="wrap phero-grid">
<div>
<div class="eyebrow"><i></i>Авторский курс · мини-группа до 5 человек</div>
<h1 style="color:#fff;text-transform:uppercase;margin-bottom:22px">Азы криптовалют</h1>
<p class="lead">От «что такое блокчейн» до первой покупки, холодного кошелька и крипто-карты — вживую и под моим личным контролем</p>
<div class="hero-btns"><a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener">{TGSVG}Записаться в группу</a><a class="btn btn-ghost" href="#program">Программа</a></div>
</div>
<div class="grid" style="gap:14px">
<div class="card ink" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><h3>6 живых уроков</h3><p>Никаких записей вместо занятий — всё вживую, с вопросами по ходу.</p></div>
<div class="card ink" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><h3>До 5 человек</h3><p>Мини-группа, чтобы я успевала разобрать ситуацию каждого.</p></div>
<div class="card ink" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)"><h3>Проверяю сама</h3><p>Домашние задания проверяю лично и даю обратную связь.</p></div>
</div>
</div></section>

<section class="light">
{btc_bg(300,'10%','right','-90px',4)}
<div class="wrap">
<div class="kicker fade">Для кого</div>
<h2 class="fade">Курс для вас, если</h2>
<div class="grid g4" style="margin-top:34px">
<div class="card fade"><div class="ic">1</div><p>Давно хотите разобраться в криптовалюте, но не знаете, с чего начать</p></div>
<div class="card fade"><div class="ic">2</div><p>Боитесь ошибиться с переводом или потерять деньги из-за мошенников</p></div>
<div class="card fade"><div class="ic">3</div><p>Хотите платить криптой и переводить деньги между странами</p></div>
<div class="card fade"><div class="ic">4</div><p>Думаете об инвестициях в крипту, но пока не решились</p></div>
</div></div></section>

<section class="light" id="program" style="padding-top:20px">
<div class="wrap">
<div class="kicker fade">Программа</div>
<h2 class="fade">Шесть уроков — от основ до налогов</h2>
<p class="sub fade">В каждом уроке теория и практика: по ходу курса вы шаг за шагом настраиваете всё, что нужно для жизни с криптовалютой.</p>
<div class="lessons">{les_html}</div>
</div></section>

<section class="dark">
<canvas class="net"></canvas>{btc_bg(400,'15%','left','-120px',2)}
<div class="wrap">
<div class="kicker fade">Результат</div>
<h2 class="fade">Что у вас будет после курса</h2>
<p class="sub fade">Не просто знания, а работающая инфраструктура — настроенная вами лично под моим контролем.</p>
<div class="results fade">
<div><i>⇄</i>Аккаунт на бирже</div><div><i>🔒</i>Холодный кошелёк</div><div><i>💳</i>Крипто-карта</div><div><i>₿</i>Первая покупка</div><div><i>↗</i>Первый перевод</div>
</div>
<div class="pills" style="justify-content:center;margin-top:40px"><span class="pill">Все уроки вживую</span><span class="pill">Личная проверка домашних заданий</span><span class="pill">Все материалы остаются с вами</span></div>
</div></section>

<section class="light">
<div class="wrap" style="max-width:820px">
<div class="price pop fade" style="padding:44px;text-align:center"><span class="lbl">Мини-группа до 5 человек</span>
<h3 style="font-size:28px;text-transform:uppercase">Курс «Азы криптовалют»</h3>
<div class="val">€390</div><div class="dur">за весь курс · 6 живых уроков · домашние задания с проверкой · материалы навсегда</div>
<p>Напишите мне — расскажу о ближайшем наборе и забронирую место в группе.</p>
<a class="btn btn-blue" href="{TG}" target="_blank" rel="noopener" style="width:auto;align-self:center">{TGSVG}Узнать дату старта</a></div>
</div></section>
'''

os.makedirs('bot', exist_ok=True)
os.makedirs('crypto', exist_ok=True)
pages = {
 'index.html': page('Екатерина Павлова — международный финансовый советник', 'Екатерина Павлова, международный финансовый советник в Сербии. Личные финансы, криптовалюта, налоги, инвестиции. Бесплатная встреча-знакомство 30 минут.', 'index', '', main_body),
 'bot/index.html': page('Бюджет-ассистент — Telegram-бот для учёта финансов | Екатерина Павлова', 'Telegram-бот для учёта личных финансов и мини-бизнеса: голосовой ввод, несколько валют, Google-таблица с дашбордом. Первый месяц бесплатно.', 'bot', '../', bot_body),
 'crypto/index.html': page('Курс «Азы криптовалют» — мини-группа до 5 человек | Екатерина Павлова', 'Авторский курс Екатерины Павловой: блокчейн, биткоин, безопасность, стейблкоины, налоги. Живые уроки, проверка домашних заданий, первая покупка и холодный кошелёк.', 'crypto', '../', crypto_body),
}
for path, html in pages.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('ok', path, len(html))

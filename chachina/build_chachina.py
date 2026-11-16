# Сборка сайта chachina.fin-academy.net: RU -> index.html, SR -> sr/index.html
# Запуск из папки chachina/:  python3 build_chachina.py
import os, re

TG = "https://t.me/a_chachina"

T = {
'ru': dict(
  lang='ru', title='Анна Чачина — международное финансовое планирование',
  desc='Анна Чачина, международный финансовый консультант в Сербии. Инвестиции, страхование, пенсия, капитал детям, переводы и криптовалюта. Бесплатная встреча-знакомство 30 минут.',
  langsw='<b>RU</b><a href="sr/" hreflang="sr">SR</a>', img='anna.jpg',
  brand='Анна Чачина', brand_sub='Финансовый консультант · Сербия',
  nav_q='Вопросы', nav_f='Форматы', nav_p='Сопровождение', nav_c='Контакты', book='Записаться',
  eyebrow='Международный финансовый консультант · Сербия',
  h1='Международное финансовое планирование',
  lead='Помогаю сохранить и приумножить капитал в любой стране мира',
  cta_main='Записаться на бесплатную встречу', cta_ghost='Смотреть форматы',
  first_l='Первый шаг', first_v='Встреча-знакомство · 30 мин · бесплатно',
  st1='25+', st1t='клиентов на сопровождении', st2='20+', st2t='лет в корпоративных финансах', st3='€0', st3t='первая встреча',
  about_h='Обо мне', role2='Международный финансовый советник',
  bio=['Помогаю создать пассивный доход и защитить накопления от рисков: на любой стадии жизни, в любой стране мира.',
       '6 лет в финансовом консалтинге, 50+ клиентов из Сербии, России, Нидерландов, Испании, Азии.',
       '20+ лет в финансах: руководящие позиции в Gillette, P&amp;G, Unilever, Wiener Städtische, Generali.',
       'Сертифицированный финансовый консультант, международный финансовый менеджер CIMA, член ассоциации финансовых планировщиков в РФ.'],
  exp_l='Опыт',
  exp=['<b>25+ клиентов</b> на сопровождении',
       '<b>20+ лет в корпоративных финансах:</b> руководящие позиции в Gillette, P&amp;G, Unilever',
       '<b>Эксперт по страхованию:</b> Wiener Städtische, Generali (Сербия)'],
  spec_l='Специализация',
  spec=['Защита капитала','Международные решения','Образование детей и пенсия','Денежные переводы и криптовалюта'],
  q_h='С какими вопросами ко мне приходят',
  q_sub='Если узнаёте свой вопрос — приходите на бесплатную встречу, разберём его вместе.',
  qs=['С чего начать инвестировать, если я живу за рубежом?',
      'Какого брокера выбрать с российским паспортом, чтобы минимизировать санкционные риски?',
      'Как перевести деньги в Сербию из России и других стран, в том числе через криптовалюту?',
      'Как подобрать страхование в Сербии или за рубежом и защитить семью от рисков?',
      'Как накопить на образование детей?',
      'Как обеспечить себе стабильную пенсию за рубежом?',
      'Как передать капитал детям без лишних рисков?',
      'Верна ли моя стратегия и куда двигаться дальше?',
      'Хорошо зарабатываю, но всё трачу — как начать откладывать?',
      'Как выстроить общую финансовую стратегию семьи или пары?'],
  f_h='Форматы консультаций', f_sub='Разовые встречи — когда нужен ответ на конкретный вопрос или взгляд со стороны.',
  free='Бесплатно', popular='Начните здесь', min='минут',
  f=[('Встреча-знакомство','Бесплатно','30','Обсудим ваш запрос и подберём формат взаимодействия'),
     ('Консультация','€150','60','Ответ на ваш конкретный вопрос'),
     ('Аудит финансового состояния','€150','90','Взгляд со стороны + письменные рекомендации')],
  f_btn='Записаться',
  p_h='Сопровождение по финансам', p_sub='Когда нужен не один ответ, а система: стратегия, план и поддержка во внедрении.',
  p1='Стратегическая сессия', p1p='€500', p1m='2 встречи',
  p1l=['Разбор вашей финансовой ситуации','Личная индивидуальная стратегия'],
  p2='Финансовый план', p2p='от €1 500', p2m='5 встреч за 2 месяца', p2tag='Максимум результата',
  p2l=['Полный финансовый план','Изучение инструментов','Создание финансовой стратегии для достижения ваших целей',
       'Подбор страховых и инвестиционных решений','Инструкции по открытию счетов','Менторская поддержка во внедрении стратегии'],
  how_h='Как записаться',
  how=[('Напишите в Telegram','Нажмите «Записаться» — откроется чат со мной.'),
       ('Выберем время','Договоримся о бесплатной встрече-знакомстве на 30 минут онлайн.'),
       ('Подберём формат','Обсудим ваш запрос и решим, какой формат вам подойдёт.')],
  pr_l='Обучение', pr_h='Практикум «Путь к финансовой свободе»',
  pr_t='Хотите разобраться в личных финансах самостоятельно? Вместе с Екатериной Павловой мы ведём единственный русскоязычный практикум по личным финансам и инвестициям для резидентов Сербии.',
  pr_btn='Подробнее о практикуме', pr_url='https://rs.fin-academy.net/',
  c_h='Начните с бесплатной встречи-знакомства', c_t='30 минут — разберём ваш вопрос и подберём формат.',
  foot='© 2026 Анна Чачина · Международный финансовый консультант · Сербия',
),
'sr': dict(
  lang='sr-Latn', title='Ana Čačina — međunarodno finansijsko planiranje',
  desc='Ana Čačina, međunarodni finansijski konsultant u Srbiji. Investicije, osiguranje, penzija, kapital za decu, transferi novca i kriptovalute. Besplatan upoznavni sastanak od 30 minuta.',
  langsw='<a href="../" hreflang="ru">RU</a><b>SR</b>', img='../anna.jpg',
  brand='Ana Čačina', brand_sub='Finansijski konsultant · Srbija',
  nav_q='Pitanja', nav_f='Formati', nav_p='Podrška', nav_c='Kontakt', book='Zakažite',
  eyebrow='Međunarodni finansijski konsultant · Srbija',
  h1='Međunarodno finansijsko planiranje',
  lead='Pomažem da sačuvate i uvećate kapital u bilo kojoj zemlji sveta',
  cta_main='Zakažite besplatan sastanak', cta_ghost='Pogledajte formate',
  first_l='Prvi korak', first_v='Upoznavni sastanak · 30 min · besplatno',
  st1='25+', st1t='klijenata koje vodim', st2='20+', st2t='godina u korporativnim finansijama', st3='€0', st3t='prvi sastanak',
  about_h='O meni', role2='Međunarodni finansijski savetnik',
  bio=['Pomažem da stvorite pasivni prihod i zaštitite ušteđevinu od rizika: u bilo kojoj fazi života, u bilo kojoj zemlji sveta.',
       '6 godina u finansijskom konsaltingu, 50+ klijenata iz Srbije, Rusije, Holandije, Španije, Azije.',
       '20+ godina u finansijama: rukovodeće pozicije u kompanijama Gillette, P&amp;G, Unilever, Wiener Städtische, Generali.',
       'Sertifikovani finansijski konsultant, međunarodni finansijski menadžer CIMA, član udruženja finansijskih planera u Rusiji.'],
  exp_l='Iskustvo',
  exp=['<b>25+ klijenata</b> koje stalno vodim',
       '<b>20+ godina u korporativnim finansijama:</b> rukovodeće pozicije u kompanijama Gillette, P&amp;G, Unilever',
       '<b>Ekspert za osiguranje:</b> Wiener Städtische, Generali (Srbija)'],
  spec_l='Specijalizacija',
  spec=['Zaštita kapitala','Međunarodna rešenja','Obrazovanje dece i penzija','Transferi novca i kriptovalute'],
  q_h='Sa kojim pitanjima mi dolaze',
  q_sub='Ako prepoznajete svoje pitanje — dođite na besplatan sastanak i rešićemo ga zajedno.',
  qs=['Kako da počnem da investiram ako živim u inostranstvu?',
      'Kog brokera da izaberem sa ruskim pasošem da bih smanjio rizik od sankcija?',
      'Kako da prebacim novac u Srbiju iz Rusije i drugih zemalja, uključujući i preko kriptovaluta?',
      'Kako da izaberem osiguranje u Srbiji ili inostranstvu i zaštitim porodicu od rizika?',
      'Kako da uštedim za obrazovanje dece?',
      'Kako da obezbedim stabilnu penziju u inostranstvu?',
      'Kako da prenesem kapital deci bez nepotrebnih rizika?',
      'Da li je moja strategija ispravna i kuda dalje?',
      'Dobro zarađujem, ali sve potrošim — kako da počnem da štedim?',
      'Kako da napravimo zajedničku finansijsku strategiju porodice ili para?'],
  f_h='Formati konsultacija', f_sub='Pojedinačni sastanci — kada vam treba odgovor na konkretno pitanje ili pogled sa strane.',
  free='Besplatno', popular='Počnite ovde', min='minuta',
  f=[('Upoznavni sastanak','Besplatno','30','Razgovaramo o vašem zahtevu i biramo format saradnje'),
     ('Konsultacija','€150','60','Odgovor na vaše konkretno pitanje'),
     ('Revizija finansijskog stanja','€150','90','Pogled sa strane + pisane preporuke')],
  f_btn='Zakažite',
  p_h='Finansijska podrška', p_sub='Kada vam ne treba jedan odgovor, već sistem: strategija, plan i podrška u sprovođenju.',
  p1='Strateška sesija', p1p='€500', p1m='2 sastanka',
  p1l=['Analiza vaše finansijske situacije','Lična individualna strategija'],
  p2='Finansijski plan', p2p='od €1 500', p2m='5 sastanaka za 2 meseca', p2tag='Maksimalan rezultat',
  p2l=['Kompletan finansijski plan','Upoznavanje sa instrumentima','Izrada finansijske strategije za ostvarenje vaših ciljeva',
       'Izbor rešenja za osiguranje i investiranje','Uputstva za otvaranje računa','Mentorska podrška u sprovođenju strategije'],
  how_h='Kako da zakažete',
  how=[('Pišite mi na Telegramu','Kliknite „Zakažite“ — otvoriće se čet sa mnom.'),
       ('Dogovorimo termin','Zakazujemo besplatan upoznavni sastanak od 30 minuta onlajn.'),
       ('Biramo format','Razgovaramo o vašem zahtevu i biramo format koji vam odgovara.')],
  pr_l='Obuka', pr_h='Praktikum «Put do finansijske slobode»',
  pr_t='Želite sami da se snađete u ličnim finansijama? Zajedno sa Ekaterinom Pavlovom vodim jedini praktikum na ruskom jeziku o ličnim finansijama i investicijama za rezidente Srbije.',
  pr_btn='Više o praktikumu', pr_url='https://rs.fin-academy.net/sr/',
  c_h='Počnite od besplatnog upoznavnog sastanka', c_t='30 minuta — analiziramo vaše pitanje i biramo format.',
  foot='© 2026 Ana Čačina · Međunarodni finansijski konsultant · Srbija',
),
}

TGSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M21.9 4.3 18.7 19.4c-.2 1.1-.9 1.3-1.8.8l-4.8-3.6-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.9 8.9-8c.4-.3-.1-.5-.6-.2L6.4 13.2l-4.7-1.5c-1-.3-1-1 .2-1.5L20.6 3c.9-.3 1.6.2 1.3 1.3z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="m5 12.5 4.5 4.5L19 7.5"/></svg>'

CSS = r"""
:root{--navy:#141c3a;--navy-2:#1f2a52;--navy-3:#2b3768;--copper:#b8693f;--copper-2:#d0875c;--sand:#e9c9ae;
--bg:#f6f3ee;--bg-2:#efe9e0;--card:#fff;--line:#e6dfd4;--text:#262a36;--muted:#636878}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:84px}
body{font-family:Onest,Montserrat,system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}img{display:block;max-width:100%}
h1,h2,h3{font-family:"Playfair Display",Georgia,serif;font-weight:700;line-height:1.15;color:var(--navy)}
.wrap{max-width:1140px;margin:0 auto;padding:0 24px}
section{padding:96px 0}
.kicker{font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;font-weight:600;color:var(--copper);margin-bottom:14px}
h2{font-size:clamp(30px,4vw,44px);margin-bottom:14px;max-width:20ch}
.sub{color:var(--muted);font-size:18px;max-width:60ch;margin-bottom:44px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;font:600 16px/1 inherit;font-family:inherit;text-decoration:none;padding:17px 28px;border-radius:14px;transition:background .25s,box-shadow .25s,transform .25s,color .25s;cursor:pointer}
.btn svg{width:19px;height:19px}
.btn-copper{background:var(--copper);color:#fff;box-shadow:0 10px 30px -10px rgba(184,105,63,.7)}
.btn-copper:hover{background:var(--copper-2);transform:translateY(-2px)}
.btn-ghost{color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.35)}
.btn-ghost:hover{box-shadow:inset 0 0 0 1px #fff;background:rgba(255,255,255,.06)}
.btn-navy{background:var(--navy);color:#fff}.btn-navy:hover{background:var(--navy-3)}
.btn-line{color:var(--navy);box-shadow:inset 0 0 0 1.5px var(--navy)}.btn-line:hover{background:var(--navy);color:#fff}

/* header */
header{position:fixed;inset:0 0 auto;z-index:50;background:rgba(20,28,58,.92);backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.08)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:20px;color:#fff}
.brand{text-decoration:none;line-height:1.2}
.brand b{font-family:"Playfair Display",Georgia,serif;font-size:19px;font-weight:700;display:block}
.brand span{font-size:12.5px;color:rgba(255,255,255,.6)}
.nav ul{display:flex;gap:28px;list-style:none;font-size:15px}
.nav ul a{text-decoration:none;color:rgba(255,255,255,.72);transition:color .2s}.nav ul a:hover{color:#fff}
.nav-r{display:flex;align-items:center;gap:16px}
.lang{display:flex;gap:4px;font-size:14px;font-weight:500}
.lang a,.lang b{padding:6px 10px;border-radius:8px;text-decoration:none}
.lang a{color:rgba(255,255,255,.65)}.lang a:hover{color:#fff}
.lang b{background:var(--sand);color:var(--navy);font-weight:700}
.nav .btn{padding:11px 18px;font-size:15px}
@media(max-width:960px){.nav ul{display:none}}
@media(max-width:520px){.nav .btn{display:none}.brand span{display:none}}

/* hero */
.hero{background:radial-gradient(1100px 520px at 85% 10%,rgba(184,105,63,.28),transparent 60%),radial-gradient(800px 500px at 0% 100%,rgba(70,90,170,.35),transparent 60%),var(--navy);color:#fff;padding:150px 0 0;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.3fr .7fr;gap:40px;align-items:end}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:14px;color:var(--sand);border:1px solid rgba(233,201,174,.3);padding:8px 16px;border-radius:999px;margin-bottom:26px}
.eyebrow i{width:8px;height:8px;border-radius:50%;background:var(--copper-2);box-shadow:0 0 0 4px rgba(208,135,92,.25)}
.hero h1{color:#fff;font-size:clamp(38px,5.6vw,66px);max-width:14ch;margin-bottom:22px}
.hero .lead{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-size:clamp(19px,2vw,23px);color:rgba(255,255,255,.85);max-width:32ch;margin-bottom:36px}
.hero-btns{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:56px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid rgba(255,255,255,.14);padding:26px 0 40px;gap:20px}
.stats b{font-family:"Playfair Display",Georgia,serif;font-size:36px;color:var(--sand);display:block;line-height:1.1}
.stats span{font-size:14px;color:rgba(255,255,255,.65)}
.photo{position:relative;align-self:end;justify-self:center;width:100%;max-width:380px}
.photo::before{content:"";position:absolute;inset:-18px -18px auto auto;width:70%;height:70%;border:1.5px solid rgba(233,201,174,.45);border-radius:22px}
.photo img{position:relative;width:100%;aspect-ratio:382/450;object-fit:cover;border-radius:22px 22px 0 0;box-shadow:0 30px 70px -20px rgba(0,0,0,.6)}
.badge{position:absolute;left:-28px;bottom:36px;background:#fff;color:var(--navy);border-radius:16px;padding:14px 18px;box-shadow:0 20px 40px -14px rgba(0,0,0,.45);max-width:290px}
.badge small{display:block;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--copper);font-weight:700}
.badge span{font-weight:600;font-size:15px;line-height:1.35}
@media(max-width:900px){.hero{padding-top:120px}.hero-grid{grid-template-columns:1fr}.photo{max-width:320px;margin-top:10px}.badge{left:auto;right:-10px}}
@media(max-width:560px){.stats b{font-size:28px}.badge{position:static;margin:14px 0 30px;max-width:none}.photo img{border-radius:22px}.photo::before{display:none}}

/* about */
.about{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
.box{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:32px}
.box h3{font-family:Onest,system-ui,sans-serif;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:18px}
ul.ticks{list-style:none;display:grid;gap:12px}
ul.ticks li{display:flex;gap:12px;align-items:flex-start}
ul.ticks li svg{flex:none;width:22px;height:22px;color:#fff;background:var(--copper);border-radius:50%;padding:4px;margin-top:2px}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chips span{background:var(--bg);border:1px solid var(--line);border-radius:999px;padding:10px 18px;font-weight:500}
@media(max-width:800px){.about{grid-template-columns:1fr}}

.bio{max-width:820px}
.bio img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:24px;box-shadow:0 30px 60px -30px rgba(20,28,58,.45)}
.role2{color:var(--copper);font-weight:600;font-size:18px;margin-bottom:10px}
.insta{display:inline-flex;align-items:center;gap:8px;color:var(--navy);text-decoration:none;font-weight:500;margin-bottom:22px;border-bottom:1px solid var(--line)}
.insta:hover{color:var(--copper)}
.bio-lead{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-size:21px;color:var(--navy);line-height:1.45;margin-bottom:22px}
.spec{margin-top:28px}
.spec h3{font-family:Onest,system-ui,sans-serif;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:14px}
.chips span{background:#fff}
@media(max-width:860px){.bio{grid-template-columns:1fr;gap:30px}.bio img{max-width:420px}}
/* questions */
.qsec{background:var(--bg-2)}
.qs{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:14px;counter-reset:q}
.qs li{counter-increment:q;display:flex;gap:18px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;transition:transform .25s,box-shadow .25s,border-color .25s}
.qs li:hover{transform:translateY(-3px);box-shadow:0 18px 40px -22px rgba(20,28,58,.35);border-color:var(--sand)}
.qs li::before{content:counter(q,decimal-leading-zero);font-family:"Playfair Display",Georgia,serif;color:var(--copper);font-size:24px;line-height:1.1;min-width:34px}
@media(max-width:800px){.qs{grid-template-columns:1fr}}

/* formats */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.fmt{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:30px;display:flex;flex-direction:column;position:relative;transition:transform .25s,box-shadow .25s}
.fmt:hover{transform:translateY(-4px);box-shadow:0 24px 50px -26px rgba(20,28,58,.4)}
.fmt.hl{border:2px solid var(--copper)}
.tag{position:absolute;top:-13px;left:26px;background:var(--copper);color:#fff;font-size:12px;font-weight:700;letter-spacing:.06em;padding:5px 12px;border-radius:999px}
.fmt h3{font-family:Onest,system-ui,sans-serif;font-size:19px;font-weight:700;min-height:2.4em}
.price{font-family:"Playfair Display",Georgia,serif;color:var(--copper);font-size:40px;font-weight:700;line-height:1.1;margin:14px 0 4px}
.dur{display:inline-flex;align-items:center;gap:8px;color:var(--muted);font-weight:500;font-size:15px;margin-bottom:16px}
.dur::before{content:"";width:8px;height:8px;border-radius:50%;border:2px solid var(--copper)}
.fmt p{color:var(--text);flex:1;margin-bottom:24px}
.fmt .btn{width:100%}
@media(max-width:900px){.grid3{grid-template-columns:1fr}.fmt h3{min-height:0}}

/* packages */
.psec{background:var(--navy);color:#fff;background-image:radial-gradient(900px 500px at 100% 0%,rgba(184,105,63,.22),transparent 60%)}
.psec h2{color:#fff}.psec .sub{color:rgba(255,255,255,.7)}.psec .kicker{color:var(--sand)}
.grid2{display:grid;grid-template-columns:1fr 1.35fr;gap:22px;align-items:stretch}
.pkg{background:var(--navy-2);border:1px solid rgba(255,255,255,.1);border-radius:22px;padding:34px;display:flex;flex-direction:column;position:relative}
.pkg.main{background:#fff;color:var(--text);border:0}
.pkg .tag{background:var(--sand);color:var(--navy)}
.pkg h3{font-family:Onest,system-ui,sans-serif;font-size:22px;font-weight:700;color:inherit}
.pkg .price{font-size:44px;color:var(--sand)}.pkg.main .price{color:var(--copper)}
.pkg .dur{color:rgba(255,255,255,.65)}.pkg.main .dur{color:var(--muted)}
.pkg ul{list-style:none;display:grid;gap:12px;margin:6px 0 30px;flex:1}
.pkg.main ul{grid-template-columns:1fr 1fr;column-gap:24px;align-content:start}
.pkg li{display:flex;gap:12px;align-items:flex-start}
.pkg li svg{flex:none;width:22px;height:22px;color:var(--navy);background:var(--sand);border-radius:50%;padding:4px;margin-top:2px}
.pkg.main li svg{color:#fff;background:var(--copper)}
.pkg ol{list-style:none;counter-reset:s;display:grid;gap:14px;margin:6px 0 30px;flex:1;align-content:start}
.pkg ol li{counter-increment:s}
.pkg ol li::before{content:counter(s);flex:none;width:30px;height:30px;border-radius:50%;border:1.5px solid var(--sand);color:var(--sand);display:grid;place-items:center;font-weight:700;font-size:14px}
.pkg .btn-ghost{align-self:flex-start}
@media(max-width:900px){.grid2{grid-template-columns:1fr}.pkg.main ul{grid-template-columns:1fr}}

/* how */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;counter-reset:h}
.step{counter-increment:h;padding:28px 26px;border-radius:20px;background:var(--card);border:1px solid var(--line)}
.step::before{content:counter(h);display:grid;place-items:center;width:46px;height:46px;border-radius:14px;background:var(--navy);color:var(--sand);font-family:"Playfair Display",Georgia,serif;font-size:22px;font-weight:700;margin-bottom:18px}
.step h3{font-family:Onest,system-ui,sans-serif;font-size:19px;margin-bottom:6px}
.step p{color:var(--muted)}
@media(max-width:800px){.steps{grid-template-columns:1fr}}

/* practicum */
.prac{display:grid;grid-template-columns:1.4fr auto;gap:30px;align-items:center;background:linear-gradient(120deg,#fff,#fbf6f0);border:1px solid var(--line);border-radius:24px;padding:40px 44px}
.prac h2{font-size:clamp(26px,3vw,34px);max-width:none}
.prac p{color:var(--muted);max-width:62ch}
@media(max-width:800px){.prac{grid-template-columns:1fr;padding:30px 26px}}

/* final cta */
.final{padding:0 0 96px}
.cta{background:var(--navy);color:#fff;border-radius:28px;padding:56px 48px;display:flex;justify-content:space-between;align-items:center;gap:30px;flex-wrap:wrap;background-image:radial-gradient(700px 300px at 100% 100%,rgba(184,105,63,.4),transparent 60%)}
.cta h2{color:#fff;margin-bottom:8px}
.cta p{color:rgba(255,255,255,.75);font-size:18px}
footer{background:#0e1430;color:rgba(255,255,255,.6);padding:30px 0;font-size:14px}
footer .wrap{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap}
footer a{color:#fff;text-decoration:none}
.fade{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}
.fade.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.fade{opacity:1;transform:none}*{transition:none!important}}
"""

def page(d):
    tg = f'href="{TG}" target="_blank" rel="noopener"'
    ticks = lambda items: ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in items)
    fmts = ''
    for i,(n,p,m,t) in enumerate(d['f']):
        hl = ' hl' if i == 0 else ''
        tag = f'<span class="tag">{d["popular"]}</span>' if i == 0 else ''
        btn = 'btn-copper' if i == 0 else 'btn-line'
        fmts += f'<div class="fmt{hl} fade">{tag}<h3>{n}</h3><div class="price">{p}</div><div class="dur">{m} {d["min"]}</div><p>{t}</p><a class="btn {btn}" {tg}>{TGSVG}{d["f_btn"]}</a></div>'
    steps = ''.join(f'<div class="step fade"><h3>{a}</h3><p>{b}</p></div>' for a,b in d['how'])
    qs = ''.join(f'<li class="fade">{q}</li>' for q in d['qs'])
    chips = ''.join(f'<span>{x}</span>' for x in d['spec'])
    alt = 'https://chachina.fin-academy.net/'
    return f'''<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['title']}</title>
<meta name="description" content="{d['desc']}">
<meta property="og:type" content="website">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['desc']}">
<meta property="og:image" content="https://chachina.fin-academy.net/anna.jpg">
<link rel="alternate" hreflang="ru" href="{alt}">
<link rel="alternate" hreflang="sr" href="{alt}sr/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap nav">
  <a class="brand" href="#top"><b>{d['brand']}</b><span>{d['brand_sub']}</span></a>
  <ul><li><a href="#questions">{d['nav_q']}</a></li><li><a href="#formats">{d['nav_f']}</a></li><li><a href="#support">{d['nav_p']}</a></li><li><a href="#contacts">{d['nav_c']}</a></li></ul>
  <div class="nav-r"><div class="lang">{d['langsw']}</div><a class="btn btn-copper" {tg}>{d['book']}</a></div>
</div></header>

<section class="hero" id="top"><div class="wrap hero-grid">
  <div>
    <div class="eyebrow"><i></i>{d['eyebrow']}</div>
    <h1>{d['h1']}</h1>
    <p class="lead">{d['lead']}</p>
    <div class="hero-btns"><a class="btn btn-copper" {tg}>{TGSVG}{d['cta_main']}</a><a class="btn btn-ghost" href="#formats">{d['cta_ghost']}</a></div>
    <div class="stats"><div><b>{d['st1']}</b><span>{d['st1t']}</span></div><div><b>{d['st2']}</b><span>{d['st2t']}</span></div><div><b>{d['st3']}</b><span>{d['st3t']}</span></div></div>
  </div>
  <div class="photo"><img src="{d['img']}" alt="{d['brand']}" width="382" height="450"><div class="badge"><small>{d['first_l']}</small><span>{d['first_v']}</span></div></div>
</div></section>

<section id="about"><div class="wrap">
  <div class="bio fade">
    <div>
      <div class="kicker">{d['about_h']}</div>
      <h2 style="margin-bottom:6px">{d['brand']}</h2>
      <div class="role2">{d['role2']}</div>
      <a class="insta" href="https://www.instagram.com/anna.finance.invest/" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></svg>@anna.finance.invest</a>
      <p class="bio-lead">{d['bio'][0]}</p>
      <ul class="ticks">{ticks(d['bio'][1:])}</ul>
      <div class="spec"><h3>{d['spec_l']}</h3><div class="chips">{chips}</div></div>
    </div>
  </div>
</div></section>

<section class="qsec" id="questions"><div class="wrap">
  <h2>{d['q_h']}</h2><p class="sub">{d['q_sub']}</p>
  <ol class="qs">{qs}</ol>
</div></section>

<section id="formats"><div class="wrap">
  <h2>{d['f_h']}</h2><p class="sub">{d['f_sub']}</p>
  <div class="grid3">{fmts}</div>
</div></section>

<section class="psec" id="support"><div class="wrap">
  <h2>{d['p_h']}</h2><p class="sub">{d['p_sub']}</p>
  <div class="grid2">
    <div class="pkg fade"><h3>{d['p1']}</h3><div class="price">{d['p1p']}</div><div class="dur">{d['p1m']}</div>
      <ol>{''.join(f'<li style="display:flex;gap:12px;align-items:center">{x}</li>' for x in d['p1l'])}</ol>
      <a class="btn btn-ghost" {tg}>{TGSVG}{d['f_btn']}</a></div>
    <div class="pkg main fade"><span class="tag">{d['p2tag']}</span><h3>{d['p2']}</h3><div class="price">{d['p2p']}</div><div class="dur">{d['p2m']}</div>
      <ul>{ticks(d['p2l'])}</ul>
      <a class="btn btn-copper" {tg} style="align-self:flex-start">{TGSVG}{d['f_btn']}</a></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2 style="margin-bottom:34px">{d['how_h']}</h2>
  <div class="steps">{steps}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="prac fade"><div><div class="kicker">{d['pr_l']}</div><h2>{d['pr_h']}</h2><p>{d['pr_t']}</p></div>
  <a class="btn btn-navy" href="{d['pr_url']}" target="_blank" rel="noopener">{d['pr_btn']} →</a></div>
</div></section>

<section class="final" id="contacts"><div class="wrap">
  <div class="cta"><div><h2>{d['c_h']}</h2><p>{d['c_t']}</p></div>
  <a class="btn btn-copper" {tg}>{TGSVG}Telegram @a_chachina</a></div>
</div></section>

<footer><div class="wrap"><span>{d['foot']}</span><a {tg}>Telegram @a_chachina</a></div></footer>
<script>
(function(){{try{{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});
document.querySelectorAll('.fade').forEach(function(el){{io.observe(el)}})}}catch(e){{document.querySelectorAll('.fade').forEach(function(el){{el.classList.add('in')}})}}}})();
</script>
</body>
</html>'''

here = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(here, 'index.html'), 'w').write(page(T['ru']))
os.makedirs(os.path.join(here, 'sr'), exist_ok=True)
sr = page(T['sr'])
open(os.path.join(here, 'sr', 'index.html'), 'w').write(sr)
body = re.sub(r'<style>.*?</style>|<script>.*?</script>', '', sr, flags=re.S)
print('ok; cyrillic left in SR:', re.findall(r'[А-Яа-яЁё]{3,}', body))

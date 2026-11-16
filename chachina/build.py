# Собирает chachina/index.html (RU) и chachina/sr/index.html (SR) из одного шаблона.
# Запуск: python3 chachina/build.py
import os, re
D = os.path.dirname(os.path.abspath(__file__))
TG = "https://t.me/a_chachina"

RU = dict(
 lang="ru", title="Анна Чачина — международное финансовое планирование",
 desc="Анна Чачина, международный финансовый консультант в Сербии. Помогаю сохранить и приумножить капитал в любой стране мира. Бесплатная встреча-знакомство 30 минут.",
 langsw='<b>RU</b><a href="sr/" hreflang="sr">SR</a>', img="anna.jpg", base="",
 brand_sub="Международный финансовый консультант",
 nav1="Обо мне", nav2="Вопросы", nav3="Тарифы", book="Записаться",
 kicker="Сербия · онлайн по всему миру",
 h1="Международное финансовое планирование",
 lead="Помогаю сохранить и приумножить капитал в любой стране мира",
 hl1="Инвестиции и брокеры для тех, кто живёт за рубежом", hl2="Страхование, пенсия и образование детей", hl3="Переводы денег, в том числе через криптовалюту",
 cta_main="Бесплатная встреча · 30 мин", cta_ghost="Смотреть тарифы",
 photo_name="Анна Чачина", photo_role="Финансовый консультант · Сербия",
 f1b="25+", f1="клиентов на сопровождении", f2b="20+", f2="лет в корпоративных финансах", f3b="3", f3="мировые корпорации: Gillette, P&amp;G, Unilever", f4b="2", f4="страховые компании в Сербии: Wiener Städtische, Generali",
 about_h="Обо мне", about_p="Больше 20 лет я работала на руководящих позициях в корпоративных финансах Gillette, P&amp;G и Unilever, а потом стала экспертом по страхованию в Сербии. Сейчас помогаю семьям, которые живут за рубежом, выстроить понятную финансовую систему: защитить то, что уже есть, и спокойно копить на большие цели.",
 spec_h="Специализация", s1="Защита капитала", s2="Международные решения", s3="Образование детей и пенсия", s4="Денежные переводы и криптовалюта",
 q_h="С какими вопросами ко мне приходят",
 q=["С чего начать инвестировать, если я живу за рубежом?",
    "Какого брокера выбрать с российским паспортом, чтобы минимизировать санкционные риски?",
    "Как перевести деньги в Сербию из России и других стран, в том числе через криптовалюту?",
    "Как подобрать страхование в Сербии или за рубежом и защитить семью от рисков?",
    "Как накопить на образование детей?",
    "Как обеспечить себе стабильную пенсию за рубежом?",
    "Как передать капитал детям без лишних рисков?",
    "Верна ли моя стратегия и куда двигаться дальше?",
    "Хорошо зарабатываю, но всё трачу — как начать откладывать?",
    "Как выстроить общую финансовую стратегию семьи или пары?"],
 fmt_h="Форматы консультаций", fmt_sub="Начните с бесплатной встречи — обсудим ваш запрос и подберём подходящий формат.",
 c1="Встреча-знакомство", c1p="Бесплатно", c1d="30 минут", c1t="Обсудим ваш запрос и подберём формат взаимодействия", c1tag="Первый шаг",
 c2="Консультация", c2p="€150", c2d="60 минут", c2t="Ответ на ваш конкретный вопрос",
 c3="Аудит финансового состояния", c3p="€150", c3d="90 минут", c3t="Взгляд со стороны + письменные рекомендации",
 sup_h="Сопровождение по финансам",
 p1="Стратегическая сессия", p1p="€500", p1d="2 встречи", p1a="Разбор вашей финансовой ситуации", p1b="Личная индивидуальная стратегия",
 p2="Финансовый план", p2p="от €1 500", p2d="5 встреч за 2 месяца", p2tag="Полное сопровождение",
 p2l=["Полный финансовый план","Создание финансовой стратегии для достижения ваших целей","Подбор страховых и инвестиционных решений","Изучение инструментов","Инструкции по открытию счетов","Менторская поддержка во внедрении стратегии"],
 choose="Записаться",
 how_h="Как записаться", st1="Напишите мне в Telegram", st2="Договоримся о времени бесплатной встречи", st3="За 30 минут разберём ваш запрос и выберем формат",
 fin_h="Начните с бесплатной встречи-знакомства", fin_p="30 минут — разберём ваш вопрос и подберём формат.",
 tg_btn="Написать в Telegram", foot="Международный финансовый консультант · Сербия", fin_ac="Курс ФинАкадемии «Путь к финансовой свободе»",
)

SR = dict(
 lang="sr-Latn", title="Ana Čačina — međunarodno finansijsko planiranje",
 desc="Ana Čačina, međunarodni finansijski savetnik u Srbiji. Pomažem da sačuvate i uvećate kapital u bilo kojoj zemlji sveta. Besplatan upoznavni sastanak od 30 minuta.",
 langsw='<a href="../" hreflang="ru">RU</a><b>SR</b>', img="../anna.jpg", base="../",
 brand_sub="Međunarodni finansijski savetnik",
 nav1="O meni", nav2="Pitanja", nav3="Cene", book="Zakažite",
 kicker="Srbija · onlajn širom sveta",
 h1="Međunarodno finansijsko planiranje",
 lead="Pomažem da sačuvate i uvećate kapital u bilo kojoj zemlji sveta",
 hl1="Investicije i brokeri za one koji žive u inostranstvu", hl2="Osiguranje, penzija i obrazovanje dece", hl3="Transfer novca, uključujući i kriptovalute",
 cta_main="Besplatan sastanak · 30 min", cta_ghost="Pogledajte cene",
 photo_name="Ana Čačina", photo_role="Finansijski savetnik · Srbija",
 f1b="25+", f1="klijenata koje pratim", f2b="20+", f2="godina u korporativnim finansijama", f3b="3", f3="svetske kompanije: Gillette, P&amp;G, Unilever", f4b="2", f4="osiguravajuće kuće u Srbiji: Wiener Städtische, Generali",
 about_h="O meni", about_p="Više od 20 godina radila sam na rukovodećim pozicijama u korporativnim finansijama kompanija Gillette, P&amp;G i Unilever, a zatim postala stručnjak za osiguranje u Srbiji. Danas pomažem porodicama koje žive u inostranstvu da izgrade jasan finansijski sistem: da zaštite ono što već imaju i mirno štede za velike ciljeve.",
 spec_h="Specijalizacija", s1="Zaštita kapitala", s2="Međunarodna rešenja", s3="Obrazovanje dece i penzija", s4="Transfer novca i kriptovalute",
 q_h="Sa kojim pitanjima mi se obraćaju",
 q=["Kako početi sa investiranjem ako živim u inostranstvu?",
    "Kog brokera izabrati sa ruskim pasošem da bih smanjio rizik od sankcija?",
    "Kako preneti novac u Srbiju iz Rusije i drugih zemalja, uključujući i preko kriptovaluta?",
    "Kako izabrati osiguranje u Srbiji ili inostranstvu i zaštititi porodicu od rizika?",
    "Kako uštedeti za obrazovanje dece?",
    "Kako obezbediti stabilnu penziju u inostranstvu?",
    "Kako preneti kapital deci bez nepotrebnih rizika?",
    "Da li je moja strategija ispravna i kuda dalje?",
    "Dobro zarađujem, ali sve potrošim — kako početi da štedim?",
    "Kako izgraditi zajedničku finansijsku strategiju porodice ili para?"],
 fmt_h="Formati konsultacija", fmt_sub="Počnite od besplatnog sastanka — razgovaraćemo o vašem pitanju i izabrati pravi format.",
 c1="Upoznavni sastanak", c1p="Besplatno", c1d="30 minuta", c1t="Razgovaramo o vašem pitanju i biramo format saradnje", c1tag="Prvi korak",
 c2="Konsultacija", c2p="€150", c2d="60 minuta", c2t="Odgovor na vaše konkretno pitanje",
 c3="Revizija finansijskog stanja", c3p="€150", c3d="90 minuta", c3t="Pogled sa strane + pisane preporuke",
 sup_h="Finansijsko praćenje",
 p1="Strateška sesija", p1p="€500", p1d="2 sastanka", p1a="Analiza vaše finansijske situacije", p1b="Lična individualna strategija",
 p2="Finansijski plan", p2p="od €1 500", p2d="5 sastanaka za 2 meseca", p2tag="Potpuno praćenje",
 p2l=["Kompletan finansijski plan","Izrada finansijske strategije za postizanje vaših ciljeva","Izbor rešenja za osiguranje i investiranje","Upoznavanje sa instrumentima","Uputstva za otvaranje računa","Mentorska podrška u sprovođenju strategije"],
 choose="Zakažite",
 how_h="Kako da zakažete", st1="Pišite mi na Telegram", st2="Dogovorićemo termin besplatnog sastanka", st3="Za 30 minuta analiziramo vaše pitanje i biramo format",
 fin_h="Počnite od besplatnog upoznavnog sastanka", fin_p="30 minuta — analiziramo vaše pitanje i biramo format.",
 tg_btn="Pišite na Telegram", foot="Međunarodni finansijski savetnik · Srbija", fin_ac="Kurs FinAkademije „Put do finansijske slobode“",
)

TPL = open(os.path.join(D, "template.html"), encoding="utf-8").read()

def render(t):
    t = dict(t)
    t["tg"] = TG
    t["fin_url"] = "https://rs.fin-academy.net/" + ("" if t["lang"] == "ru" else "sr/")
    t["qs"] = "\n".join(f"      <li>{x}</li>" for x in t.pop("q"))
    t["p2list"] = "\n".join(f"          <li>{x}</li>" for x in t.pop("p2l"))
    out = TPL
    for k, v in t.items():
        out = out.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{\w+\}\}", out)
    assert not left, left
    return out

open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(render(RU))
os.makedirs(os.path.join(D, "sr"), exist_ok=True)
open(os.path.join(D, "sr", "index.html"), "w", encoding="utf-8").write(render(SR))
print("ok")

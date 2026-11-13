import re,base64,io,os
from PIL import Image
from sr_dict import SR
t=open('template.html').read()
def enc(im,w,q=84):
    im=im.convert('RGB')
    if im.width>w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
    b=io.BytesIO();im.save(b,'JPEG',quality=q,optimize=True);return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
poster=Image.open('/mnt/user-data/uploads/b1e42452-image.png')
imgs={'{HERO}':enc(poster.crop((60,215,1020,748)),1200),'{EK}':enc(Image.open('/tmp/pp/s19_4.png'),800),'{AN}':enc(Image.open('/home/claude/site/anna.png'),800)}
ru=t.replace('{LANGSW}','<b>RU</b><a href="sr/" hreflang="sr">SR</a>')
sr=t.replace('{LANGSW}','<a href="../" hreflang="ru">RU</a><b>SR</b>').replace('<html lang="ru">','<html lang="sr-Latn">')
missing=set()
def tr(m):
    pre,txt,post=m.group(1),m.group(2),m.group(3)
    if re.search('[А-Яа-яЁё]',txt):
        if txt in SR: return '>'+pre+SR[txt]+post+'<'
        missing.add(txt)
    return m.group(0)
head,rest=sr.split('<script>',1)
head=re.sub(r'>(\s*)([^<>]*?[^<>\s])(\s*)<',tr,head)
def tra(m):
    v=m.group(2)
    if re.search('[А-Яа-яЁё]',v):
        if v in SR: return m.group(1)+'="'+SR[v]+'"'
        missing.add(v)
    return m.group(0)
head=re.sub(r'\b(alt|placeholder|aria-label|data-plan|content|value)="([^"]*)"',tra,head)
for k in ['Отправляем…','Не получилось отправить заявку. Напишите нам в Telegram:']:
    rest=rest.replace(k,SR[k])
sr=head+'<script>'+rest
print('missing:',missing)
for k,v in imgs.items(): ru=ru.replace(k,v); sr=sr.replace(k,v)
open('index.html','w').write(ru); os.makedirs('sr',exist_ok=True); open('sr/index.html','w').write(sr)
import re as r2; print('cyr left in sr:', len(r2.findall('[А-Яа-яЁё]{3,}', sr.split('<script>')[0].split('<style>')[0]+sr.split('</style>')[1].split('<script>')[0])))

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
from pathlib import Path
import os
base=Path(r'C:\Users\Home\Documents\ChatGPT\prospecção\012-store-jacarei-conceito')
W,H=1800,1200
paper='#f1efe8'; ink='#171919'; lime='#d3ef36'; muted='#66665f'
im=Image.new('RGB',(W,H),paper); d=ImageDraw.Draw(im)
def font(name,size):
    for p in [r'C:\Windows\Fonts\arialbd.ttf' if name=='bold' else r'C:\Windows\Fonts\arial.ttf']:
        try:return ImageFont.truetype(p,size)
        except:pass
    return ImageFont.load_default()
try: mono=ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf',14)
except: mono=font('',14)
d.text((62,35),'012  STORE · SURF WEAR',font=font('bold',36),fill=ink)
d.text((1170,54),'VITRINE CONCEITUAL  ·  JACAREÍ/SP  ·  09 NOV 2026',font=mono,fill=ink)
d.line((62,96,1738,96),fill='#aaa89f',width=2)
d.text((62,119),'UMA REFERÊNCIA. TRÊS CAMINHOS DE DESCOBERTA.',font=font('bold',36),fill=ink)
d.text((62,174),'Cinco referências distintas, organizadas para descobrir peças e consultar a equipe com contexto.',font=font('',16),fill=muted)
assets=['catalog-tech-fleece.jpg','catalog-polos.jpg','catalog-tnf-set.jpg']
labels=['01  EDITORIAL · HISTÓRIA E SELEÇÃO','02  LOJA DIRETA · BUSCA E CATEGORIAS','03  LOOKBOOK · IMAGEM E COMBINAÇÃO']
for i,(asset,label) in enumerate(zip(assets,labels)):
    x=62+i*562
    d.rectangle((x,210,x+540,966),outline='#aaa89f',width=2)
    d.text((x+12,220),label,font=mono,fill=ink)
    photo=Image.open(base/'assets'/asset).convert('RGB')
    photo=ImageOps.fit(photo,(524,700),method=Image.Resampling.LANCZOS)
    im.paste(photo,(x+8,250))
    shade=Image.new('RGBA',(500,240),(15,17,17,190)); im.paste(shade,(x+20,690),shade); d=ImageDraw.Draw(im)
    titles=[('O SEU RITMO. A SUA RUA.','5 referências únicas · consulte com a 012'),('ENCONTRE. CONSULTE.','Busca · categorias · ordenação'),('PEÇAS QUE SEGUEM COM VOCÊ.','Detalhes · origem · consulta')]
    d.text((x+36,728),titles[i][0],font=font('bold',26),fill='white')
    d.text((x+36,780),titles[i][1],font=font('',15),fill='white')
d.line((62,990,1738,990),fill='#aaa89f',width=2)
d.text((62,1010),'CONCEITO INDEPENDENTE · Imagens do perfil oficial; não confirmam estoque atual. Valores, tamanhos e atacado devem ser',font=font('',14),fill=muted)
d.text((62,1033),'consultados diretamente com a loja. Sem pagamento ou integração de estoque.',font=font('',14),fill=muted)
d.text((62,1072),'INSTAGRAM @012STORESURFWEAR_   ·   WHATSAPP +55 12 99232-3004',font=mono,fill=ink)
im.save(base/'arte'/'012-store-prancha.png',quality=95)

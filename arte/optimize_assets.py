from pathlib import Path
from PIL import Image
base=Path(r'C:\Users\Home\Documents\ChatGPT\prospecção\012-store-jacarei-conceito')
replacements={'kit-preto-01.jpg':'kit-preto-02.jpg','kit-preto-02.jpg':'kit-preto-02.jpg','kit-preto-produto.jpg':'kit-preto-01.jpg','look-camiseta-01.jpg':'detalhe-kit-02.jpg','look-camiseta-02.jpg':'detalhe-kit-01.jpg','look-camiseta-03.jpg':'look-camiseta-03.jpg','look-camiseta-04.jpg':'kit-preto-01.jpg'}
for target,source in replacements.items():
 im=Image.open(base/'assets'/source).convert('RGB'); im.thumbnail((1500,1800),Image.Resampling.LANCZOS); im.save(base/'assets'/target,'JPEG',quality=86,optimize=True,progressive=True)

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


BASE = Path(__file__).resolve().parents[1]
OUTPUT = BASE / 'arte' / '012-store-prancha.png'
WIDTH, HEIGHT = 1600, 1200
PAPER = '#F8F6F1'
CARD = '#FFFEFC'
INK = '#302D2C'
MUTED = '#77716C'
LINE = '#DDD8D1'
OLIVE = '#65703A'
LIME = '#D3EF36'

canvas = Image.new('RGB', (WIDTH, HEIGHT), PAPER)
draw = ImageDraw.Draw(canvas)


def font(filename, size):
    return ImageFont.truetype(Path(r'C:\Windows\Fonts') / filename, size)


serif = lambda size: font('georgia.ttf', size)
serif_bold = lambda size: font('georgiab.ttf', size)
sans = lambda size: font('arial.ttf', size)
sans_bold = lambda size: font('arialbd.ttf', size)
mono = lambda size: font('consola.ttf', size)


def fitted_image(filename, box, focus=(0.5, 0.5)):
    image = Image.open(BASE / 'assets' / filename).convert('RGB')
    image = ImageOps.fit(image, box[2:], method=Image.Resampling.LANCZOS, centering=focus)
    canvas.paste(image, box[:2])


def label(x, y, text, color=OLIVE, size=11):
    draw.text((x, y), text.upper(), font=mono(size), fill=color)


margin = 72

# Brand line
draw.text((margin, 43), '012', font=serif_bold(32), fill=INK)
draw.text((142, 57), 'STORE · SURF WEAR', font=sans_bold(15), fill=INK)
draw.text((658, 59), 'SURFWEAR · JACAREÍ / SP', font=mono(11), fill=MUTED)
label(1365, 59, 'Prévia conceitual', color=INK, size=10)
draw.line((margin, 105, WIDTH - margin, 105), fill=LINE, width=1)

# Intro and a non-catalog photo keep all five product references distinct below.
label(margin, 151, 'Uma vitrine no ritmo da 012', size=11)
draw.text((margin, 189), 'Mais contexto para', font=serif(53), fill=INK)
draw.text((margin, 248), 'escolher. Mais simples', font=serif(53), fill=INK)
draw.text((margin, 307), 'para chamar.', font=serif(53), fill=INK)
draw.multiline_text(
    (margin, 389),
    'Uma proposta de catálogo complementar para organizar referências\n'
    'publicadas pela 012 e levar a conversa para o WhatsApp com a peça\n'
    'que chamou atenção.',
    font=sans(16), fill=MUTED, spacing=9,
)
draw.rectangle((margin, 485, margin + 315, 518), outline=OLIVE, width=1)
label(margin + 12, 495, 'Fotos de referência · estoque a confirmar', size=9)

fitted_image('loja-012.jpg', (925, 150, 603, 366), focus=(0.5, 0.45))
draw.rectangle((925, 150, 1528, 516), outline=LINE, width=1)

# Three concise concept cards. The five different catalog photos appear once each.
cards = [
    {
        'x': 72,
        'label': '01 · Editorial',
        'title': 'Campanha e narrativa',
        'body': 'Uma abertura visual para apresentar\na identidade da 012.',
        'images': [('catalog-tech-fleece.jpg', (0.5, 0.35))],
    },
    {
        'x': 564,
        'label': '02 · Loja direta',
        'title': 'Busca e categorias',
        'body': 'Filtros e detalhes para encontrar\numa referência e perguntar por ela.',
        'images': [
            ('catalog-polos.jpg', (0.5, 0.52)),
            ('catalog-sneakers.jpg', (0.5, 0.5)),
        ],
    },
    {
        'x': 1056,
        'label': '03 · Lookbook',
        'title': 'Looks em sequência',
        'body': 'Duas referências diferentes; escolha\no que curtiu e consulte a loja.',
        'images': [
            ('catalog-tnf-set.jpg', (0.5, 0.52)),
            ('catalog-quiksilver-set.jpg', (0.5, 0.48)),
        ],
    },
]
card_width, card_top, card_bottom = 472, 552, 881
for card in cards:
    x = card['x']
    draw.rectangle((x, card_top, x + card_width, card_bottom), fill=CARD, outline=LINE, width=1)
    label(x + 15, card_top + 13, card['label'], size=10)
    photo_y, photo_h = card_top + 40, 170
    images = card['images']
    if len(images) == 1:
        fitted_image(images[0][0], (x + 14, photo_y, card_width - 28, photo_h), images[0][1])
    else:
        gap, inset = 7, 14
        tile_width = (card_width - inset * 2 - gap) // 2
        for index, (filename, focus) in enumerate(images):
            fitted_image(filename, (x + inset + index * (tile_width + gap), photo_y, tile_width, photo_h), focus)
    draw.text((x + 15, photo_y + photo_h + 12), card['title'], font=serif(22), fill=INK)
    draw.multiline_text((x + 15, photo_y + photo_h + 48), card['body'], font=sans(12), fill=MUTED, spacing=5)

# Practical rationale in the two-column structure of the supplied examples.
summary_y = 921
draw.line((margin, summary_y - 16, WIDTH - margin, summary_y - 16), fill=LINE, width=1)
label(margin, summary_y, 'Três estruturas, uma identidade', color=INK, size=10)
draw.text((margin, summary_y + 23), 'Editorial, loja direta e lookbook', font=serif(22), fill=INK)
draw.multiline_text(
    (margin, summary_y + 59),
    'A pessoa escolhe como explorar: uma entrada com narrativa, uma busca\n'
    'objetiva por categoria ou uma apresentação visual de referências.',
    font=sans(12), fill=MUTED, spacing=6,
)

right_x = 818
label(right_x, summary_y, 'Um começo melhor para a conversa', color=INK, size=10)
draw.text((right_x, summary_y + 23), 'Referência escolhida, consulta direta', font=serif(22), fill=INK)
draw.multiline_text(
    (right_x, summary_y + 59),
    'A seleção prepara uma mensagem no WhatsApp. Preço, variações e\n'
    'disponibilidade ficam com a equipe; não há estoque integrado.',
    font=sans(12), fill=MUTED, spacing=6,
)

# Signal-lime swatch retains a quiet link to the site's visual identity.
for index, color in enumerate((PAPER, INK, OLIVE, LIME)):
    x = margin + index * 37
    draw.ellipse((x, 1061, x + 25, 1086), fill=color, outline=LINE, width=1)

draw.line((margin, 1103, WIDTH - margin, 1103), fill=LINE, width=1)
draw.text((margin, 1120), '012 STORE · PROTÓTIPO DE EXPERIÊNCIA', font=sans(9), fill=MUTED)
draw.text((622, 1120), 'Imagens de referência · estoque e valores a confirmar', font=sans(9), fill=MUTED)
draw.text((1280, 1120), 'Apresentação conceitual · ServAgency', font=sans(9), fill=MUTED)

canvas.save(OUTPUT, optimize=True)
print(f'Prancha gerada: {OUTPUT} ({WIDTH}x{HEIGHT})')

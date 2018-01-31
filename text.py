# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('simsun.ttc',24)
base = Image.open('e3.jpg').convert('RGBA')
txt = Image.new('RGBA', base.size, (255,255,255,0))
text = "你好！"
draw = ImageDraw.Draw(txt)
draw.text((20, 20),text, fill=(255,255,255),font=font)
out = Image.alpha_composite(base, txt)

out.show()
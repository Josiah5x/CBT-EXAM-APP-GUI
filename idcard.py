from tkinter import Image, font
from PIL import Image, ImageDraw, ImageFont

template =Image.open('idcard.PNG')
myimage = Image.open('img/ww.webp').resize((100, 100), Image.ANTIALIAS)

template.paste(myimage, (10, 10, 190, 265))
# draw = ImageDraw.Draw(template)
# text = 'Josiah Livinus Chuntan'
# font = ImageFont.truetype('HungryCharlie-Bold.ttf')
# draw.text((468,340), text, fill=('yellow'))
myimage.save('tex4.jpeg')
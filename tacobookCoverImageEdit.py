'''
Reginald Zaccardi-Richey
TacoBook Cover Image Editor
'''


'''

'''
from PIL import Image, ImageDraw, ImageFont

image = Image.open('tacoCover2.jfif')

image.thumbnail((400,800))

imageDraw = ImageDraw.Draw(image)

font = ImageFont.truetype('DejaVuSans.ttf', 50)
imageDraw.text([20, 25], 'RANDOM\nTACO\nCOOKBOOK', fill='DarkViolet', font=font)
# save new image
image.save('tacobookCover.jpeg')
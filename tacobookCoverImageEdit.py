'''
Reginald Zaccardi-Richey
TacoBook Cover Image Editor
'''


'''

'''
from PIL import Image, ImageDraw, ImageFont

image = Image.open('tacoBOI.jpg')

image.thumbnail((800,800))

imageDraw = ImageDraw.Draw(image)

font = ImageFont.truetype('DejaVuSans.ttf', 25)
imageDraw.text([200, 25], 'RANDOM\nTACO RECIPE\nCOOKBOOK', fill='Fuchsia', font=font)
# save new image
image.save('tacobookCover.jpeg')
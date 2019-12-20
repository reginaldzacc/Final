'''
Reginald Zaccardi-Richey
TacoBook Cover Image Editor
'''


'''
This short program takes a saved image,
opens the image, resizes the image to a 
smaller size,then writes RANDOM TACO 
COOKBOOK on the image
'''
from PIL import Image, ImageDraw, ImageFont
image = Image.open('tacoCover2.jfif')#opens saved cover image
image.thumbnail((500,500))#resize image to 500x500
imageDraw = ImageDraw.Draw(image)#allows drawing on image
font = ImageFont.truetype('DejaVuSans.ttf', 50)#creates a font to use
imageDraw.text([20, 25], 'RANDOM\nTACO\nCOOKBOOK', fill='DarkViolet', font=font)#writes title on image using font variable
image.save('tacobookCover.jpeg')#save new image
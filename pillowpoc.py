#!/usr/bin/python3
from PIL import Image

img = Image.open('test2.bmp').resize((212, 104))
pixels = list(img.getdata())

threshold = 10

newPixels = []
for pixel in pixels:
    if pixel[0] <= threshold:
        newPixel = (255, 255, 255)
    else:
        newPixel = (0, 0, 0)
    newPixels.append(newPixel)

newImg = Image.new(img.mode, img.size)
newImg.putdata(newPixels)

newImg.show()
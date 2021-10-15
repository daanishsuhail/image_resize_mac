import os, sys
from PIL import Image 
import random

x = 2560 
y = 1600 

x_follower = 0
y_follower = 0
randomizer = 0

img = Image.new(mode="RGB", size = (x,y), color = (255,255,255))

img.save("bg.png")

while(y_follower <= y-1):
    a = random.randint(0,1)
    if(a == 1):
        img.putpixel((x_follower, y_follower), (0,0,0))
    x_follower += 1 
    if(x_follower == x-1):
        x_follower = 0
        y_follower += 1
    
img.save("temp.png")

image = Image.open("temp.png")
image = image.convert("RGBA")
datas = image.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

image.putdata(newData)
image.save("maxwall.png", "PNG")

image.size

image = image.resize((2457, 1536), Image.ANTIALIAS)
image.save("scaled_miniwall.png", quality=95)

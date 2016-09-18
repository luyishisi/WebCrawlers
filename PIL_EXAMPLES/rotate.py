# coding:utf-8
from PIL import Image
import glob, os

size = 128,128

# 打开图片
im = Image.open("1.png")
# 旋转45度 并且 显示

# im.rotate(45).show()

# 遍历该目录下的所有PNG文件，打开并且创建略缩图
for infile in glob.glob("*.png"):
    file,ext = os.path.splitext(infile)
    print file,ext
    im = Image.open(infile)
    im.thumbnail(size,Image.ANTIALIAS)
    im.save(file+".thumbnail","JPEG")

# 创建新图片，并保存
new_img = Image.new("RGB",(512,512),"white")
new_img.save("NEW.png")

im_2 = Image.open("2.png")

#im_3 = Image.composite(im,im_2,RGBA)
im_compound = Image.blend(im.copy().load(),im_2.copy().load(),0.0)
im_compound.save("3.png")

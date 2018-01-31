from PIL import Image

imageFName = 'e3.jpg'

def image_transpose(image): 
    xsize, ysize = image.size
    xsizeLeft = xsize//2

    boxLeft = (0, 0, xsizeLeft, ysize)
    boxRight = (xsizeLeft, 0, xsize, ysize)
    boxLeftNew = (0,0,xsizeLeft,ysize)
    boxRightNew = (xsizeLeft, 0, xsize, ysize)

    print(boxLeft, boxRight, boxLeftNew, boxRightNew)
    partLeft = image.crop(boxLeft).transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)
    partRight = image.crop(boxRight)

    image.paste(partRight,boxLeftNew)
    image.paste(partLeft, boxRightNew)

    return image

avatar = Image.open(imageFName)
avatar = image_transpose(avatar)
avatar.show()
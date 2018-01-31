from PIL import Image
sourceFileName = "e3.jpg"
avatar = Image.open(sourceFileName)
print(avatar.format, avatar.size, avatar.mode)
avatar.show()
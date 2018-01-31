import os, sys
from PIL import Image

print(sys.argv[1:])
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + '.thumbnail'+ os.path.splitext(infile)[1]
    if infile != outfile:
        im = Image.open(infile)
        x, y = im.size
        print(os.path.splitext(infile)[0],infile,outfile,x,y)        
        im.thumbnail((x/2, y/2))
        im.save(outfile, im.format)    
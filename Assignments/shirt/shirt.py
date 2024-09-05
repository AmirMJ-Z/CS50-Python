import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments ')

try:
    image = Image.open(sys.argv[1])

except:
    sys.exit('Invalid input')

if sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
    sys.exit('Input and output have different extensions')

shirt = Image.open('shirt.png')
size = shirt.size

image = ImageOps.fit(image, size)
image.paste(shirt, shirt)

image.save(
    sys.argv[2]
)



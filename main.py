from PIL import Image
from dictionary import blockRGB
import time

start_time = time.time()

diff = 100000
tempDiff = 0
closeKey = 1
prefix = r"C:\Users\Minglun\PycharmProjects\Minecraft convert\block"
path = ""
rgb_pixel_value = [0, 0, 0]
smolEdgeLen = 0
ratio = 0
imageName = ""
newImageName = ""

imageName = input("enter the image name:\n")
image = Image.open(imageName)
smolEdgeLen = int(input("enter the length for the smaller edge:\n"))
newImageName = input("Name of file(with file type):\n")

if image.width < image.height:
    ratio = smolEdgeLen / image.width
    image = image.resize((smolEdgeLen, round(image.height * ratio)))
elif image.height < image.width:
    ratio = smolEdgeLen / image.height
    image = image.resize((round(image.width * ratio), smolEdgeLen))
else:
    image = image.resize((smolEdgeLen, smolEdgeLen))

collage = Image.new("RGB", (image.width * 16, image.height * 16))
for x in range(image.width):
    for y in range(image.height):
        rgb_pixel_value = image.getpixel((x, y))
        rgb_pixel_value = list(rgb_pixel_value)
        for k, key in enumerate(blockRGB):
            for l in range(3):
                tempDiff += abs(rgb_pixel_value[l] - blockRGB[key][l])
            tempDiff = round(tempDiff / 3)
            if tempDiff < diff:
                diff = tempDiff
                closeKey = key
            if diff < 10:
                break
            tempDiff = 0
        diff = 256
        path = prefix + r"\ "[:-1] + closeKey
        block = Image.open(path)
        collage.paste(block, (x*16, y*16))
    print(x, "/", image.width)
collage.save(newImageName)
collage.show()
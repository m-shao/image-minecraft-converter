import cv2
import numpy
import os

temp = 0

for image in os.listdir(r"C:\Users\Minglun\PycharmProjects\Minecraft convert\block"):
    prefix = r"C:\Users\Minglun\PycharmProjects\Minecraft convert\block"
    path = prefix + r"\ "[:-1] + image
    myimg = cv2.imread(path)
    avg_color_per_row = numpy.average(myimg, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    avg_color = list(avg_color)
    temp = avg_color[0]
    avg_color[0] = avg_color[-1]
    avg_color[-1] = temp
    print("    " + "\"" + image + "\"" + ": ", avg_color, ",")
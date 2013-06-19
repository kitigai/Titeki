#coding:utf-8
import sys
import numpy
import cv2
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt

argvs = sys.argv
if (len(argvs) != 3):
	print "miss"
	quit()

imagefilename = argvs[1]
matrix = argvs[2]
pgm = pgmdat()
pgm.readimg(imagefilename)
img = pgm.img
width = pgm.width
height = pgm.height

if matrix == "1":
	matrix1 = [[0,128],
		   [192,64]]
elif matrix == "2":
	matrix1 = [[0,128,32,160],
		   [192,64,224,96],
		   [48,176,16,144],
		   [240,112,208,80]]


plt.imshow(img)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

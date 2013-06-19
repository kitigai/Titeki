#coding:utf-8
import sys
import numpy as np
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
	matrix1 = np.array([[0,128],
		   [192,64]])
elif matrix == "2":
	matrix1 = np.array([[0,128,32,160],
		   [192,64,224,96],
		   [48,176,16,144],
		   [240,112,208,80]])

aa =  matrix1.shape
matH,matW =  aa[0],aa[1]
print matW,matH
print width,height
for i in range(0,height,matH):
	for j in range(0,width,matW):
		for H in range(matH):
			for W in range(matW):
				if img[i + H][j + W] < matrix1[H][W]:
					img[i + H][j + W] = 0
				else:
					img[i + H][j + W] = 255
plt.imshow(img)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

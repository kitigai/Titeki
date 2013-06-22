#coding:utf-8
"""ノイズ除去"""
import sys
import numpy as np
import cv2
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt

argvs = sys.argv
if (len(argvs) != 2):
	print "miss"
	quit()

imagefilename = argvs[1]
pgm = pgmdat()
pgm.readimg(imagefilename)
img = pgm.img
width = pgm.width
height = pgm.height


fix = np.zeros([height,width])
fix2 = np.zeros([height,width])

matrix = np.array([[0,-1,0],
		   [-1,5,-1],
		   [0,-1,0]])

for i in range(0,height ):
	for j in range(0,width ):

		if (i == 0) or (j == 0) or (i == height - 1) or (j == width -1):
			fix[i][j] = img[i][j]
		else:
			sum = 0
			for h in range(-1,2):
				for w in range(-1,2):
					sum += img[i + h][j + w]

			fix[i][j] = sum



for i in range(0,height ):
	for j in range(0,width ):

		if (i == 0) or (j == 0) or (i == height - 1) or (j == width -1):
			fix2[i][j] = fix[i][j]
		else:
			sum = 0
			for h in range(-1,2):
				for w in range(-1,2):
					sum += fix[i + h][j + w] * matrix[h+1][w+1]

			fix2[i][j] = sum

plt.imshow(fix2)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

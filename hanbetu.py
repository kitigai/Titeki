#coding:utf-8
"""判別分析"""
import sys
import numpy as np
import cv2
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt
def hanbe(imagefilename):
	pgm = pgmdat()
	pgm.readimg(imagefilename)
	img = pgm.img
	width = pgm.width
	height = pgm.height
	N = width * height
	print height, width,pgm.depth

	t = 0
	fix = np.zeros([height,width])
	histdata = [0] * (pgm.depth+1)
	T = 0
	tes1 = 0

	for x in range(height):
		for y in range(width):
			n = img[x][y]
			histdata[n] += 1

	Ph = [double(p)/N for p in histdata]
	U = 0
	for j in range(255):
		U += j*Ph[j]


	Ramda = 0
	ramda = 0
	for t in range(255):
		w = 0
		u = 0
		for k in range(t+1):
			w += Ph[k]
			u += k*Ph[k]
		if w  > 0:
			ramda = (U*w - u)**2/(w*(1-w))
		if ramda > Ramda:
			Ramda = ramda
			T = t
				
			
	print T
	for H in range(height):
		for W in range(width):
			if img[H][W] < T:
				fix[H][W] = 0
			else:
				fix[H][W] = 255


	return fix

if __name__ == "__main__":
	argvs = sys.argv
	if (len(argvs) != 2):
		print "miss"
		quit()

	imagefilename = argvs[1]
	fix = hanbe(imagefilename)
	plt.imshow(fix)
	plt.gray()
	plt.show()
	#cv2.imshow("tes",img)
	#cv2.waitKey(0)

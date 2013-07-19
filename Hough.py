#coding:utf-8
"""[課題1]Hough変換"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt

XMAX = 320
YMAX = 240
RMAX = 60
THETA_MAX = 1024
RHO_MAX

def Hough(img):
	



if __name__ == "__main__":

	argvs = sys.argv
	if (len(argvs) != 2):
		print "miss"
		quit()

	imagefilename = argvs[1]
	pgm = pgmdat()
	pgm.readimg(imagefilename)
	img = pgm.img


	fix,wave0 = d2wave(img,2)
	print len(fix)

	#fix = np.array([[255]*width]*height)
	plt.imshow(fix[1])
	plt.gray()
	plt.show()
	#cv2.imshow("tes",img)
	#cv2.waitKey(0)

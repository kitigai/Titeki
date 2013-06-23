#coding:utf-8
"""輪郭追跡"""
import sys
import numpy as np
import cv2
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt
import hanbetu

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
N = width * height
#niti = hanbetu.hanbe(imagefilename)
"""
matrix =       [[6,5,4],
		[7,?,3],
		[0,1,2]]
"""
fix = [[255]*width]*height

for h in range(height):
	for w in range(width):
		if img[h][w] == 255 and fix[h][w] != 0:
			print h,w
			fix[h][w] = 0
			Ph = h
			Pw = w
			H = h
			W = w
			d = 0
			f = 0
			I = 0
			while f != 1:
				if d == 0:
					d = 1
					nh = 1
					nw = -1
				elif d == 1:
					d = 2
					nh = 1
					nw = 0
				elif d == 2:
					d = 3
					nh = 1
					nw = 1
				elif d == 3:
					d = 4
					nh = 0
					nw = 1
				elif d == 4:
					d = 5
					nh = -1
					nw = 1
				elif d == 5:
					d = 6
					nh = -1
					nw = 0
				elif d == 6:
					d = 7
					nh = -1
					nw = -1
				elif d == 7:
					d = 0
					nh = 0
					nw = -1


				if H+nh < height and  W+nw < width:
					if img[H+nh][W+nw] == 255:
						I += 1
						H = H+nh
						W = W+nw
						if I == 1:
							HI = H
							WI = W
						fix[H][W] == 0
						d = ( d + 6)%8
						if  H == Ph and W== Pw and I != 1:
							print I
							f = 1
						
				else:
					f = 1	
					
plt.imshow(fix)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

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
print height,width
#niti = hanbetu.hanbe(imagefilename)
"""
matrix =       [[6,5,4],
		[7,?,3],
		[0,1,2]]
"""
fix = [[255]*width]*height

for h in range(height):
	for w in range(width):
		if img[h][w] == 255 and fix[h][w] != 0 :
			Ph = h
			Pw = w
			fix[h][w] = 0
			d = 0
			f = 0
			print h,w
			while Ph != h or Pw != w or f == 0:
				if Ph > height-2 or Pw >width-2:
					break
					
				if d == 0:
					if img[Ph+1][Pw-1] != 0:
						fix[Ph+1][Pw-1] = 0
						Ph = Ph+1
						Pw = Pw-1
						d = (d + 6)%8
						f = 1
					else:
						d = 1
				if d == 1:
					if img[Ph+1][Pw] != 0:
						fix[Ph+1][Pw] = 0
						Ph = Ph+1
						d = (d + 6)%8
						f = 1
					else:
						d = 2		
				if d == 2:
					if img[Ph+1][Pw+1] != 0:
						fix[Ph+1][Pw+1] = 0
						Ph,Pw = Ph+1,Pw+1
						d = (d + 6)%8
						f = 1
					else:
						d = 3

				if d == 3:
					if img[Ph][Pw+1] != 0:
						fix[Ph][Pw+1] = 0
						Pw = Pw+1
						d = (d + 6)%8
						f = 1
					else:
						d = 4
				if d == 4:
					if img[Ph-1][Pw+1] != 0:
						fix[Ph-1][Pw+1] = 0
						Ph,Pw = Ph-1,Pw+1
						d = (d + 6)%8
						f = 1
					else:
						d = 5
				if d == 5:
					if img[Ph-1][Pw] != 0:
						fix[Ph-1][Pw] = 0
						Ph = Ph-1
						d = (d + 6)%8
						f = 1
					else:
						d = 6
				if d == 6:
					if img[Ph-1][Pw-1] != 0:
						fix[Ph-1][Pw-1] = 0
						Ph,Pw = Ph-1,Pw-1
						d = (d + 6)%8
						f = 1
					else:
						d = 7
				if d == 7:
					if img[Ph][Pw-1] != 0:
						fix[Ph][Pw-1] = 0
						Pw = Pw-1
						d = (d + 6)%8
						f = 1
					else:
						d = 0

					
plt.imshow(fix)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

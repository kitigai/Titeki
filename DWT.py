#coding:utf-8
"""[課題1]ハールウエーブレット解析"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
import copy
import matplotlib.pyplot as plt


def upscale(c1,d1):
	N1,N2 = len(c1),len(d1)
	N = N1+N2
	c0 = np.zeros(N)
	for n in range(N/2):
		c0[2*n + 0] = c1[n]+d1[n]
		c0[2*i + 1] = c1[n]-d1[n]

	return c0

def IDWT(c):
	N,M = c.shape
	for n  in range(N):
		cn = copy.deepcopy(c[n][0:M/2])
		dn = copy.deepcopy(c[n][M/2:M])
		c[n] = upscale(cn,dn)

	c = c.T

	for m in range(M):
		

	



def downscale(c0):
	N = len(c0)
	c1 = np.zeros(N/2)
	d1 = np.zeros(N/2)
	
	for i in range(N/2):
		c1[i] = (c0[2*i] + c0[2*i + 1]) / 2.0
		d1[i] = (c0[2*i] - c0[2*i + 1]) / 2.0

	return c1,d1

def DWT(c):
	N,M = c.shape
	c1 = np.zeros([N,M])
	for n in range(N):
		cn,dn = downscale(c[n])
		c1[n] = np.hstack((cn,dn))



	c1 = c1.T

	for m in range(M):
		cn,dn = downscale(c1[m])
		c1[m] = np.hstack((cn,dn))

	c1 = c1.T
	return c1
	
		
			
	
def DWTloop(c, Nsize, Msize):
	#c1 = np.zeros([Nsize,Msize])
	c1 = c[0:Nsize,0:Msize]

	c1 = DWT(c1)


	c[0:Nsize,0:Msize] = c1
	return c

	
	
	

if __name__ == "__main__":

	argvs = sys.argv
	if (len(argvs) != 3):
		print "miss"
		quit()

	imagefilename = argvs[1]
	pgm = pgmdat()
	pgm.readimg(imagefilename)
	img = pgm.img
	width = pgm.width
	height = pgm.height


	level = int(argvs[2])
	for i in range(level):
		img = DWTloop(img,height,width)
		height /= 2
		width /= 2
	#fix = np.array([[255]*width]*height)
	plt.imshow(img)
	plt.gray()
	plt.show()
	#cv2.imshow("tes",img)
	#cv2.waitKey(0)

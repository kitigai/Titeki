#coding:utf-8
import numpy as np

def dct(x):
	N = len(x)
	X = [0]*N
	for k in range(N):
		for l in range(N):
			X[k] += x[l]*np.cos(np.pi*k*(2*l+1)/(2*N))
		X[k]  = X[k]*2/N

	return X

def idct(X):
	N = len(X)
	x = [0]*N
	for l in range(N):
		x[l] += X[0]/2
		for k in range(1,N):
			x[l] += X[k]*np.cos(np.pi*k*(2*l+1)/(2*N))
		x[l] = int(x[l]+0.5)
	return x

if __name__ == "__main__":
	import sys
	from pylab import *
	from pypgm import pgmdat
	import matplotlib.pyplot as plt
	from copy import deepcopy

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
	fix = np.ones([height,width])
	ifix = np.ones([height,width])

	for h in range(0,height,8):
		for w in range(0,width,8):
			pre = deepcopy(img[h:h+8,w:w+8])
			for dh in range(8):
				pre[dh] = dct(pre[dh])
			#pre = deepcopy(pre.T)
			#for dw in range(8):
			#	pre[dw][:] = dct(pre[dw])
			#pre = deepcopy(pre.T)
			fix[h:h+8,w:w+8] = deepcopy(pre)


	for h in range(0,height,8):
		for w in range(0,width,8):
			ipre = deepcopy(fix[h:h+8,w:w+8])
			for dh in range(8):
				ipre[dh] = idct(ipre[dh])
			#pre = deepcopy(pre.T)
			#for dw in range(8):
			#	pre[dw][:] = idct(pre[dw])
			ifix[h:h+8,w:w+8] = deepcopy(ipre)
		
	plt.imshow(ifix)
	plt.gray()
	plt.show()	
			
					

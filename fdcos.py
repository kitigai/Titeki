#coding:utf-8
import numpy as np
"""課題５　離散コサイン変換"""

def alp(k,N):
	if k == 0:
		return  np.sqrt(1.0/N)
	else:
		return np.sqrt(2.0/N)

def dct(x):
#離散コサイン変換一次元用
	N = len(x)
	X = [0]*N
	for k in range(N):
		for l in range(N):
			X[k] += x[l]*np.cos(np.pi*k*(2*l+1)/(2*N))
		X[k]  = X[k]*2/N

	return X

def dct2(f):
#離散コサイン変換二次元用
	M,N = f.shape
	F = np.zeros([M,N])	
	for u in range(M):
		for v in range(N):
			for m in range(M):
				for n in range(N):
					F[u][v] += f[m][n]*np.cos(np.pi*u*(2*m+1)/(2*M))*np.cos(np.pi*v*(2*n+1)/(2*N))
				
			F[u][v] = int(alp(u,N)*alp(v,N)*F[u][v]/10 + 0.5)*10#10の倍数に丸める


	return F

def idct(X):
#逆離散コサイン変換一次元用
	N = len(X)
	x = [0]*N
	for l in range(N):
		x[l] += X[0]/2
		for k in range(1,N):
			x[l] += X[k]*np.cos(np.pi*k*(2*l+1)/(2*N))
		x[l] = x[l]
	return x

def idct2(F):
#逆離散コサイン変換二次元用
	M,N = F.shape
	f = np.zeros([M,N])	
	for m in range(M):
		for n in range(N):
			for u in range(M):
				for v in range(N):
					f[m][n] += alp(u,N)*alp(v,N)*F[u][v]*np.cos(np.pi*u*(2*m+1)/(2*M))*np.cos(np.pi*v*(2*n+1)/(2*N))


	return f
				
if __name__ == "__main__":
	import sys
	from pylab import *
	from pypgm import pgmdat
	import matplotlib.pyplot as plt
	from copy import deepcopy
	import cv2

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
	ifix = np.ones([height,width],dtype=int)

	#離散コサイン変換ループ
	for h in range(0,height,8):
		for w in range(0,width,8):
			fix[h:h+8,w:w+8] = dct2(img[h:h+8,w:w+8])

	#逆離散コサインループ
	for h in range(0,height,8):
		for w in range(0,width,8):
			ifix[h:h+8,w:w+8] = idct2(fix[h:h+8,w:w+8])

			#ipre = deepcopy(fix[h:h+8,w:w+8])
			#for dh in range(8):
			#	ifix[h:h+8,w:w+8][dh] = idct(fix[h:h+8,w:w+8].T[dh])
			#pre = deepcopy(pre.T)
			#for dw in range(8):
			#	ifix[h:h+8,w:w+8][dw] = idct(ifix[h:h+8,w:w+8].T[dw])
			#for dw in range(8):
			#	pre[dw][:] = idct(pre[dw])
			#ifix[h:h+8,w:w+8] = deepcopy(ipre)

	cv2.imwrite("dct.pgm",ifix)
	plt.imshow(ifix)
	plt.gray()
	plt.show()	
			
					

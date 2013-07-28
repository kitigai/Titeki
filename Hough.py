#coding:utf-8
"""[課題1]Hough変換"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt
#XMAX = 320
#YMAX = 240
THETA_MAX = 128 
#RHO_MAX = 400
PIK = np.pi / THETA_MAX

def DHT(img,N,M):

	RHO_MAX = int(np.sqrt(N**2 + M**2))
	sn = []
	cs = []
	rho = 0
	
	for i in range(THETA_MAX):
		sn.append(np.sin(PIK*i))
		cs.append(np.cos(PIK*i))


	counter = np.zeros([THETA_MAX,2*RHO_MAX])

	for y in range(N):
		for x in range(M):
			if img[y][x] != 0:
				for theta in range(THETA_MAX):
					rho = int(x*cs[theta] + y*sn[theta] + 0.5)	
					counter[theta][rho+RHO_MAX] += 1	



	sikiiti = 35	
	fix = np.zeros([N,M])
	ym,xm = 0,0
	for theta_m in range(THETA_MAX):
		for rho_m in range(-RHO_MAX,RHO_MAX):
			if(counter[theta_m][rho_m+RHO_MAX] >= sikiiti):


				for xm in range(M):
					#y = int(-(cs[theta]/sn[theta] * x  + rho/sn[theta]))
					ym = uint8((rho_m - xm*cs[theta_m])/sn[theta_m])
					if(ym < N and ym >= 0):
						fix[y][x] = 255

				for ym in range(N):
					xm = int((rho_m - ym*sn[theta_m])/cs[theta_m])
					if(xm < M and xm >= 0):
						fix[ym][xm] = 255 


	return counter,fix


if __name__ == "__main__":

	argvs = sys.argv
	if (len(argvs) != 2):
		print "miss"
		quit()

	imagefilename = argvs[1]
	pgm = pgmdat()
	pgm.readimg(imagefilename)
	img = pgm.img
	height = pgm.height
	width = pgm.width
	counter,fix = DHT(img,height,width)


	#fix = np.array([[255]*width]*height)
	subplot(121)
	plt.imshow(img)
	plt.gray()
	subplot(122)
	plt.imshow(fix)
	plt.show()
	#cv2.imshow("tes",img)
	#cv2.waitKey(0)

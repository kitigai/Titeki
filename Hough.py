#coding:utf-8
"""[課題1]Hough変換"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt
#XMAX = 320
#YMAX = 240
RMAX = 60
THETA_MAX = 1024
#RHO_MAX = 400
PIK = numpy.pi / THETA_MAX

def Hough(img,N,M):

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

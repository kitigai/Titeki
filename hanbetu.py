#coding:utf-8
"""[課題３]判別分析"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
import matplotlib.pyplot as plt
import cv2
def hanbe(imagefilename):
#判別分析法処理関数	
#imagefilename	:処理画像ファイル名
#返り値:二値化結果の二次元画素配列

	pgm = pgmdat()
	pgm.readimg(imagefilename)
	img = pgm.img
	width = pgm.width
	height = pgm.height
	N = width * height
	print height, width,pgm.depth

	t = 0
	fix = np.zeros([height,width],dtype = int)
	histdata = [0] * (pgm.depth+1)
	T = 0
	tes1 = 0
	#ヒストグラム作成
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
	#クラス間分散ramdaを求めしきい値Tを最適化する
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
	#求めたしきい値Tを使って二値化
	for H in range(height):
		for W in range(width):
			if img[H][W] < T:
				fix[H][W] = 0
			else:
				fix[H][W] = 255


	return fix,img

if __name__ == "__main__":
	argvs = sys.argv
	if (len(argvs) != 2):
		print "miss"
		quit()

	imagefilename = argvs[1]
	fix,img = hanbe(imagefilename)
	print fix
	print fix.shape
	cv2.imwrite("hanbetu.pgm",fix)
	plt.imshow(fix)
	plt.gray()
	plt.show()
	#cv2.imshow("tes",img)
	#cv2.waitKey(0)

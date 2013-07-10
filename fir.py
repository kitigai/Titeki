#coding:utf-8
"""[課題２]ノイズ除去"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
import cv2
import matplotlib.pyplot as plt

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

fix = np.zeros([height+1,width+1],dtype=int)
fix2 = np.zeros([height+1,width+1],dtype=int)
#先鋭化フィルタの宣言
matrix = np.array([[0,-1,0],
		   [-1,5,-1],
		   [0,-1,0]])
#平均値フィルタの宣言
matrix2 = np.array([[1.0/9,1.0/9,1.0/9],
			[1.0/9,1.0/9,1.0/9],
			[1.0/9,1.0/9,1.0/9]])

print matrix2
#前処理として元画像に黒色の枠をつける
tatewaku = np.zeros(height,int)
yokowaku = np.zeros(width+2,int)
img = np.c_[tatewaku,img]
img = np.c_[img,tatewaku]
img = np.vstack((img,yokowaku))
img = np.vstack((yokowaku,img))

print img
#平均化処理ループ
for i in range(1,height ):
	for j in range(1,width ):

		#if (i == 0) or (j == 0) or (i == height - 1) or (j == width -1):
		#	fix[i][j] = img[i][j]
		#else:
		summ = 0
		for h in range(-1,2):
			for w in range(-1,2):
				if i == 1 and j == 1:
					print summ
				summ += img[i + h][j + w] * matrix2[h+1][w+1]#マトリクスをかける

		fix[i][j] = summ


#先鋭化処理ループ
for i in range(1,height ):
	for j in range(1,width ):
		summ = 0
		for h in range(-1,2):
			for w in range(-1,2):
				summ += fix[i + h][j + w] * matrix[h+1][w+1]#マトリクスをかける

		fix2[i][j] = summ

print fix
#cv2.imwrite("fir1.pgm",fix)
#cv2.imwrite("fir2.pgm",fix2)
#cv2.imwrite("moto.pgm",img)
plt.imshow(fix)
plt.gray()
plt.show()
plt.imshow(fix2)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

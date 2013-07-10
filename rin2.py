#coding:utf-8
"""[課題4]輪郭線追跡"""
import sys
import numpy as np
from pylab import *
from pypgm import pgmdat
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
print height,width
tatewaku = np.zeros(height)
yokowaku = np.zeros(width+2)
#前処理として元画像に黒枠をつける
img = np.c_[tatewaku,img]
img = np.c_[img,tatewaku]
img = np.vstack((img,yokowaku))
img = np.vstack((yokowaku,img))
#niti = hanbetu.hanbe(imagefilename)
"""
matrix =       [[6,5,4],
		[7,?,3],
		[0,1,2]]

探索は上記マトリクスの順番で行う
"""

#fix = np.array([[255]*width]*height)
#fix = np.identity(216)
fix = np.zeros([height,width])
print fix
#輪郭線追跡ループ
for h in range(1,height):#探索開始点探索
	for w in range(1,width):
		if img[h][w] == 255 and img[h][w-1] == 0 : 
			Ph = h
			Pw = w
			fix[h][w] = 255
			d = 0
			f = 0
			count = 0#テスト用変数、いらない
			flug = 0#テスト用変数、いらない
			coun = 0
			cPh,cPw = -1,-1#テスト用変数、いらない
			print h,w
			while Ph != h or Pw != w or f == 0 :#輪郭線追跡
				coun += 1
				if Ph == h and Pw == w and  coun == 18:#孤立点の処理
					break
			#while Ph != cPh or Pw != cPw or flug != 1:
				#if Ph == h and Pw == w and f == 1:
				#	flug = 1
					
				if Ph > height-2 or Pw > width-2:#画像端処理
					print "h"
					break
					
				if d == 0:
					if img[Ph+1][Pw-1] != 0:
						fix[Ph+1][Pw-1] = 255
						Ph = Ph+1
						Pw = Pw-1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 1
				if d == 1:
					if img[Ph+1][Pw] != 0:
						fix[Ph+1][Pw] = 255
						Ph = Ph+1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 2		
				if d == 2:
					if img[Ph+1][Pw+1] != 0:
						fix[Ph+1][Pw+1] = 255
						Ph,Pw = Ph+1,Pw+1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 3

				if d == 3:
					if img[Ph][Pw+1] != 0:
						fix[Ph][Pw+1] = 255
						Pw = Pw+1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 4
				if d == 4:
					if img[Ph-1][Pw+1] != 0:
						fix[Ph-1][Pw+1] = 255
						Ph,Pw = Ph-1,Pw+1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 5
				if d == 5:
					if img[Ph-1][Pw] != 0:
						fix[Ph-1][Pw] = 255
						Ph = Ph-1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 6
				if d == 6:
					if img[Ph-1][Pw-1] != 0:
						fix[Ph-1][Pw-1] = 255
						Ph,Pw = Ph-1,Pw-1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 7
				if d == 7:
					if img[Ph][Pw-1] != 0:
						fix[Ph][Pw-1] = 255
						Pw = Pw-1
						d = (d + 6)%8
						f = 1
						count += 1
						if count == 1:
							print count
							cPh = Ph
							cPw = Pw
					else:
						d = 0
plt.imshow(fix)
plt.gray()
plt.show()
#cv2.imshow("tes",img)
#cv2.waitKey(0)

#coding:utf-8
"""[課題4]輪郭線追跡"""
import sys
import scipy
import numpy as np
from pylab import *
from pypgm import pgmdat
import singou as sg
import matplotlib.pyplot as plt

def fcc(img,height,width):
	fix = np.zeros([height,width])
	chain = []
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
				while Ph != h or Pw != w or f == 0 :#輪郭線追跡
					coun += 1
					if Ph == h and Pw == w and  coun == 18:#孤立点の処理
						break
				#while Ph != cPh or Pw != cPw or flug != 1:
					#if Ph == h and Pw == w and f == 1:
					#	flug = 1
						
					if Ph > height-2 or Pw > width-2:#画像端処理
						break
						
					if d == 0:
						if img[Ph+1][Pw-1] != 0:
							chain.append(complex(1,-1))
							fix[Ph+1][Pw-1] = 255
							Ph = Ph+1
							Pw = Pw-1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 1
					if d == 1:
						if img[Ph+1][Pw] != 0:
							chain.append(complex(1,0))
							fix[Ph+1][Pw] = 255
							Ph = Ph+1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 2		
					if d == 2:
						if img[Ph+1][Pw+1] != 0:
							chain.append(complex(1,1))
							fix[Ph+1][Pw+1] = 255
							Ph,Pw = Ph+1,Pw+1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 3

					if d == 3:
						if img[Ph][Pw+1] != 0:
							chain.append(complex(0,1))
							fix[Ph][Pw+1] = 255
							Pw = Pw+1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 4
					if d == 4:
						if img[Ph-1][Pw+1] != 0:
							chain.append(complex(-1,1))
							fix[Ph-1][Pw+1] = 255
							Ph,Pw = Ph-1,Pw+1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 5
					if d == 5:
						if img[Ph-1][Pw] != 0:
							chain.append(complex(-1,0))
							fix[Ph-1][Pw] = 255
							Ph = Ph-1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 6
					if d == 6:
						if img[Ph-1][Pw-1] != 0:
							chain.append(complex(-1,-1))
							fix[Ph-1][Pw-1] = 255
							Ph,Pw = Ph-1,Pw-1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 7
					if d == 7:
						if img[Ph][Pw-1] != 0:
							chain.append(complex(0,-1))
							fix[Ph][Pw-1] = 255
							Pw = Pw-1
							d = (d + 6)%8
							f = 1
							count += 1
							if count == 1:
								cPh = Ph
								cPw = Pw
						else:
							d = 0

				return chain,h,w

def ifcc(chain,h,w,height,width):
	fix = np.zeros([height,width])
	fix[h,w] = 255
	for ch in chain:
		fix[h+int(ch.real),w+int(ch.imag)] = 255

	return fix
	
if __name__ == "__main__":

	argvs = sys.argv
	if (len(argvs) != 4):
		print "miss"
		quit()

	imagefilename = argvs[1]
	k = int(argvs[2])
	pgm = pgmdat()
	pgm.readimg(imagefilename)
	img = pgm.img
	width = pgm.width
	height = pgm.height
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
	samplen = int(argvs[3])
	chain2 = []
	chain,h,w = fcc(img,height,width)
	print h,w
	c = 0
	for a in range(len(chain)):
		for b in range(len(chain2)+1):
			c += chain[b]
		chain2.append(c)
		c = 0

		
	Cha = scipy.fft(chain2)
	Cha[k+1:len(Cha)-k] = [0.0]*(len(Cha)-k*2-1)
	#chreal = sg.ift(Cha)
	chreal = scipy.ifft(Cha)
	chreala = [complex(int(round(i.real)), int(round(i.imag))) for i in chreal]
	chain3 = [complex(int(round(i.real)), int(round(i.imag))) for i in chain2]
	"""
	chre = [i.real for i in chain]
	chim = [i.imag for i in chain]
	Chr = sg.dft(chre)
	Chi = sg.dft(chim)
	print len(Chr)
	Chr[k:len(Chr)-k] = [0]*(len(Chr)-k*2)
	Chi[k:len(Chi)-k] = [0]*(len(Chi)-k*2)
	chreal = sg.ift(Chr)
	chreal = [int(i.real + 0.5*i.real/np.fabs(i.real)) for i in chreal]
	chimag = sg.ift(Chi)
	chimag = [int(i.real + 0.5*i.real/np.fabs(i.real)) for i in chimag]
	cha = [complex(chreal[i],chimag[i]) for i in range(len(chimag))]
	"""
	fix = ifcc(chreala,h,w,height,width)
	fix2 = ifcc(chain3,h,w,height,width)

	chain = [ch.imag for ch in chain2]
	chreal = [chre.imag for chre in chreal]	
	chreala = [ch.imag for ch in chreala]
	chain3 = [ch.imag for ch in chain3]

	"""
	chain = [ch.real for ch in chain2]
	chreal = [chre.real for chre in chreal]	
	chreala = [ch.real for ch in chreala]
	chain3 = [ch.real for ch in chain3]
	"""
	subplot(321)
	plt.imshow(fix)
	plt.gray()
	subplot(322)
	plt.imshow(fix2)
	plt.gray()
	subplot(312)
	plot(chain)
	plot(chreal)
	plot(chreala)
	subplot(313)
	plot(chain3)
	plt.show()

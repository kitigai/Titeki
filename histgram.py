#-*- coding: utf-8 -*-
"""
	ヒストグラムグラフ作成

	使用法
	python histgram.py pgmファイル名
"""
import sys
import numpy 
from pylab import *
from pypgm import pgmdat
argvs = sys.argv
if(len(argvs) !=2 ):
	print 'miss'
	quit()

imagefilename = argvs[1]
pgm = pgmdat()
pgm.readimg(imagefilename)

width = pgm.width
height = pgm.height
depth = pgm.depth

histdata = [0] * (depth+1)

for x in range(height):
	for y in range(width):
		n = pgm.img[x][y]
		histdata[n] += 1

xl = arange(depth+1)  #ここからグラフ作成箇所
w = 0.1
hist = tuple(histdata)
print hist
bar(xl,hist,w,color='b',edgecolor='k')
#xticks(numpy.linspace(0,250,6),numpy.linspace(0,255,6))
ylabel('hist',fontname='serif')


show()


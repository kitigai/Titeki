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


def hist(img):
	histdata = [0] * (img.depth)
	for x in range(img.height):
		for y in range(img.width):
			n = img.img[x][y]
			histdata[n] += 1

	return histdata

def 
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

histdata = hist(pgm)

show()


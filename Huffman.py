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

class treenode:
	
	
	def __init__(self,value = nan,occurrence = nan,left = nan,right = nan):
		self.value = value
		self.occurrence = occurrence
		self.left = left
		self.right = right

	
def makeparents(left,right):
	occurrence = left.occurrence + right.occurrence
	parents = treenode(occurrence = occurrence,left = left,right = right)
	return parents

def madeleaf(hist):
	leaf = []	
	for h in range(len(hist)):
		leaf.append(treenode(h,hist[h]))

	leaf = sorted(leaf,key = lambda treenode: treenode.occurrence)

	return leaf

def maketree(leaf):
	allocure = 0
	for le in leaf:
		allocure += le.occurrence

		

def hist(img):
	histdata = [0] * (img.depth)
	for x in range(img.height):
		for y in range(img.width):
			n = img.img[x][y]
			histdata[n] += 1

	return histdata

if __name__ == "__main__": 
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


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
import pickle
from struct import *

class treenode:
	
	
	def __init__(self,value = None,occurrence = None,left = None,right = None,parents=None,myid = None):
		self.value = value
		self.occurrence = occurrence
		self.left = left
		self.right = right
		self.parents = parents
		self.myid = myid

	
def makeparents(left,right):
	occurrence = left.occurrence + right.occurrence
	parents = treenode(occurrence = occurrence,left = left,right = right)
	return parents

def makeleaf(hist):
	leaf = []	
	for h in range(len(hist)):
		if hist[h] != 0:
			leaf.append(treenode(h,hist[h]))

	leaf = sorted(leaf,key = lambda treenode: treenode.occurrence)

	return leaf

def maketree(leaf):
	allocure = 0
	i = 0
	for le in leaf:
		allocure += le.occurrence


	while leaf[len(leaf)-1].occurrence < allocure:	
		leaf.append(makeparents(leaf[i],leaf[i+1]))
		leaf[i].parents = leaf[len(leaf)-1]
		leaf[i].myid = "0"
		leaf[i+1].parents = leaf[len(leaf)-1]
		leaf[i+1].myid = "1"
		leaf = sorted(leaf,key = lambda treenode: treenode.occurrence)
		i += 2

	return leaf

def calkcode(leaf,value):
	for i in range(len(leaf)):
		if leaf[i].value == value:
			target = leaf[i]
	
	code ='' 
	while target.parents != None:
		code += target.myid
		target = target.parents

	code = code[::-1]

	return code
		
		

def hist(img):
	histdata = [0] * 256
	for x in range(img.height):
		for y in range(img.width):
			n = img.img[x][y]
			histdata[n] += 1

	return histdata

def savetree(tree,pgm,filename):
	f = open(filename+'.hf',"wb")
	pickle.dump(tree,f)
	height=str(pgm.height)+'\n'
	width =str(pgm.width)+'\n'
	f.write(height)
	f.write(width)

	data=''	
	for h in range(pgm.height):
		for w in range(pgm.width):
			data +=calkcode(tree,pgm.img[h][w])

	data = data+ '0'*(8-len(data)%8)
	length=len(data)/8
	print length,len(data)%8
	packed_value = pack('B'*length,int(data,2))
	f.write(packed_value)
	f.close()
		

	
	

if __name__ == "__main__": 
	argvs = sys.argv
	if(len(argvs) !=3 ):
		print 'miss'
		quit()

	imagefilename = argvs[1]
	savefilename = argvs[2]
	pgm = pgmdat()
	pgm.readimg(imagefilename)

	width = pgm.width
	height = pgm.height
	depth = pgm.depth
	img = pgm.img

	histdata = hist(pgm)
	leaf = makeleaf(histdata)
	tree = maketree(leaf)
	print 'value occurrence code'
	for x in leaf:
		code = calkcode(tree,x.value)
		print x.value, x.occurrence, code	

	savetree(tree,pgm,savefilename)


#coding:utf-8
import sys
import numpy
from pylab import *
from pypgm import pgmdat

argvs = sys.argv
if (len(argvs) != 3):
	print "miss"
	quit()

imagefilename = argvs[1]
savefilename = argvs[2]
pgm = pgmdat()
pgm.readimg(imagefilename)
width = pgm.width
height = pgm.height

matrix1 = [[0,128],
	   [192,64]]

matrix2 = [[0,128,32,160],
	   [192,64,224,96],
	   [48,176,16,144],
	   [240,112,208,80]]

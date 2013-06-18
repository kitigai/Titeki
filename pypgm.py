#-*- coding: utf-8 -*-
import struct
import re
import numpy


class pgmdat:
	"""pgm 形式の読み込み及びデータの保存クラス

   		width	: 横幅
		height	: 縦幅
		depth	: ビット深度
		img		: 二次元の画素データ配列
	"""
	def __init__(self):
		self.width = -1
		self.height = -1
		self.depth = -1
	
	
	def readimg(self,imgfilename):
		"""pgm 形式のファイルを読み込む

			imgfilename : 読み込み対象のファイル名"""
		headerflug = False
		buffer = open(imgfilename, "rb")						#とにかくバイナリとして読み込み
		buf = buffer.readlines()
		self.type = buf[0][0:2]
		for i in range(len(buf)):								#ヘッダ読み込みループ
			for x in range(len(buf[i])):						#コメントを読み飛ばし
				if buf[i][x] == '#' and headerflug == False:
					buf[i] = buf[i][0:x]
					break
		
		
			match = re.findall(r'[P0-9]+',buf[i])
				
			for n in match:
				if n[0] == 'P' and headerflug == False:
					continue	

				if self.width < 0:
					self.width = int(n)
					print self.width
				elif self.height < 0:
					self.height = int(n)
					print self.height
				elif self.depth < 0:
					self.depth = int(n)
					headerflug = True
					num = i + 1

		new = buf[num]
		for xx in range(num + 1,len(buf)):						#画素配列内に改行記号があった場合結合ji
			new = new + buf[xx]

		self.img = struct.unpack('B'*self.width*self.height,new)#バイナリを二次元数値配列に変換
		self.img = numpy.array(self.img)
		self.img = self.img.astype(numpy.uint8)
		self.img = self.img.reshape(self.height,self.width)
				
	


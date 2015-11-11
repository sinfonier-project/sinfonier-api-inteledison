#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez (@pejema44)"]
__copyright__ = "Copyright 2015, Sinfonier Project"
__maintainer__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez(@pejema44)"]
__email__ = ["eva@sinfonier-project.net","pedro@sinfonier-project.net"]
__status__ = "Beta"
__version__ = "0.1"


import sys
import mraa


sys.path.append("..")

class LightValue(object):

	def __init__(self,port):
		self.info = dict()
		self.port = port

	def getLight(self):
		lum = mraa.Aio(int(self.port))
		lumVal = float(lum.read())
		self.info["light"] = str(lumVal)
		return self.info

def testing():
	l1 = LightValue(sys.argv[1])
	print l1.getLight()

if __name__ == "__main__":
	sys.exit(testing()) 


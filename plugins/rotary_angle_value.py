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

class RotaryAngleValue(object):

	def __init__(self,port):
		self.info = dict()
		self.port = port

	def getAngle(self):
		angle = mraa.Aio(int(self.port))
		angleVal = (angle.read()*360)/1022
		self.info["angle"] = str(angleVal)
		return self.info

def testing():
	a1 = RotaryAngleValue(sys.argv[1])
	print a1.getAngle()

if __name__ == "__main__":
	sys.exit(testing()) 


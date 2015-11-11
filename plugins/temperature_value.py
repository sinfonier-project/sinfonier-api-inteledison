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
import pyupm_grove

sys.path.append("..")

class TemperatureValue(object):

	def __init__(self,port):
		self.info = dict()
		self.port = port

	def getTemp(self):
		temp = pyupm_grove.GroveTemp(int(self.port))
		tempVal = float(temp.value())
		self.info["temp"] = str(tempVal)
		return self.info

def testing():
	t1 = TemperatureValue(sys.argv[1])
	print t1.getTemp()

if __name__ == "__main__":
	sys.exit(testing()) 


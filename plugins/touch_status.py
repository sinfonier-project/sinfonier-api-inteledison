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

class TouchSensor(object):

	def __init__(self,port):
		self.info = dict()
		self.port = port

	def getTouchStatus(self):
		touch = mraa.Gpio(int(self.port))
		touch.dir(mraa.DIR_IN)
		touchstatus = int(touch.read())
		self.info["TouchSensor"] = touchstatus
		return self.info

def testing():
	b1 = TouchSensor(sys.argv[1])
	print b1.getTouchStatus()

if __name__ == "__main__":
	sys.exit(testing()) 



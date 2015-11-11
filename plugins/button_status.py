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

class Button(object):

	def __init__(self,port):
		self.info = dict()
		self.port = port

	def getButtonStatus(self):
		but = pyupm_grove.GroveButton(int(self.port))
		butstatus = int(but.value())
		self.info["button"] = butstatus
		return self.info

def testing():
	b1 = Button(sys.argv[1])
	print b1.getButtonStatus()

if __name__ == "__main__":
	sys.exit(testing()) 


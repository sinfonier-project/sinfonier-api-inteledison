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

class SwitchOnLed(object):

	def __init__(self,port,state):
		self.info = dict()
		self.info["port"] = port
		self.info["state"] = state

	def setState(self):
		led = mraa.Gpio(int(self.info["port"]))
		led.dir(mraa.DIR_OUT)
		led.write(int(self.info["state"]))
		if led.read() == 1:
			return "Encendido"
		else:
			return "Apagado"

def testing():
	l1 = SwitchOnLed(sys.argv[1],sys.argv[2])
	print l1.setState()

if __name__ == "__main__":
	sys.exit(testing()) 

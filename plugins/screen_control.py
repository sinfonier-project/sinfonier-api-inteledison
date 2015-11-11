#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez (@pejema44)"]
__copyright__ = "Copyright 2015, Sinfonier Project"
__maintainer__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez(@pejema44)"]
__email__ = ["eva@sinfonier-project.net","pedro@sinfonier-project.net"]
__status__ = "Beta"
__version__ = "0.1"


import sys

import socket
import fcntl
import struct

import pyupm_i2clcd as lcd

sys.path.append("..")

class ScreenControl(object):

	def __init__(self,r_color,g_color,b_color,x_cor,y_cor,message):
		self.info = dict()
		self.info["r"] = r_color
		self.info["g"] = g_color
		self.info["b"] = b_color
		self.info["x"] = x_cor
		self.info["y"] = y_cor
		self.info["message"] = message

	def setScreen(self):
		myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
		myLcd.clear()
		
		myLcd.setColor(int(self.info["r"]),int(self.info["g"]),int(self.info["b"]))
		myLcd.setCursor(int(self.info["y"]),int(self.info["x"]))
		myLcd.write(str(self.info["message"]))

		return "Mensaje enviado"

	def testing():
		s1 = ScreenControl(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
		print s1.setScreen()

if __name__ == "__main__":
	sys.exit(testing())



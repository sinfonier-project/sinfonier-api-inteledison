#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez (@pejema44)"]
__copyright__ = "Copyright 2015, Sinfonier Project"
__maintainer__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez(@pejema44)"]
__email__ = ["eva@sinfonier-project.net","pedro@sinfonier-project.net"]
__status__ = "Beta"
__version__ = "0.1"

import sys
import time
import pyupm_mic as upmMicrophone

sys.path.append("..")

class SoundValue(object):

	def __init__(self,port):
		self.info = dict()
		self.port = port

	def getSound(self):
		myMic = upmMicrophone.Microphone(int(self.port))
		threshContext = upmMicrophone.thresholdContext()
		threshContext.averageReading = 0
		threshContext.runningAverage = 0
		threshContext.averagedOver = 2

		buffer = upmMicrophone.uint16Array(128)
    		len = myMic.getSampledWindow(2, 128, buffer);
    		if len:
			thresh = myMic.findThreshold(threshContext, 30, buffer, len)
        		#myMic.printGraph(threshContext)
        		if(thresh):
            			print "Threshold is ", thresh
				self.info["soundLevel"] = str(thresh)
				del myMic
				return self.info

def testing():
	m1 = SoundValue(sys.argv[1])
	print m1.getTemp()

if __name__ == "__main__":
	sys.exit(testing()) 



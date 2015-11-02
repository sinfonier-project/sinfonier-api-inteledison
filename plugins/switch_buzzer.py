import sys
import mraa
import time

sys.path.append("..")

class SwitchBuzzer(object):

	def __init__(self,port,state,duration):
		self.info = dict()
		self.info["port"] = port
		self.info["state"] = state
		self.info["duration"] = duration

	def setState(self):
		buzPin = mraa.Gpio(int(self.info["port"]))
		buzPin.dir(mraa.DIR_OUT)
		buzPin.write(int(self.info["state"]))
                try:
			time.sleep(int(self.info["duration"]))
		except:
			time.sleep(2)
			pass

		if buzPin.read() == 1:
			return "Encendido"
		else:
			return "Apagado"

		buzPin.write(0)

def testing():
	b1 = SwitchBuzzer(sys.argv[1],sys.argv[2],sys.argv[3])
	print b1.setState()

if __name__ == "__main__":
	sys.exit(testing()) 


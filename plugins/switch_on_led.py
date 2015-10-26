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

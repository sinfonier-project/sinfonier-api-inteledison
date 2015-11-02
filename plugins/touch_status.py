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



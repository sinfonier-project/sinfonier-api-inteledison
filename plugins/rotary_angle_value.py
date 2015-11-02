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


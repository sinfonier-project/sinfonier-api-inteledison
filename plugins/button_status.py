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


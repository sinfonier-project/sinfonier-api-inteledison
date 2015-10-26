import sys
sys.path.append("/opt/tornado")
from plugins import (switch-on-led)

def f_switch-on-led(port,state):
	l1 = switch-on-led.SwitchOnLed(port,state)
	return l1.setState()

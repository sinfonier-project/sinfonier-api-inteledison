import sys
sys.path.append("/opt/tornado")
from plugins import (switch_on_led)

def f_switch_on_led(port,state):
	l1 = switch_on_led.SwitchOnLed(port,state)
	return l1.setState()

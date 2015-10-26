import sys
sys.path.append("/opt/tornado")
from plugins import (switch_on_led,temperature_value)

def f_switch_on_led(port,state):
	l1 = switch_on_led.SwitchOnLed(port,state)
	return l1.setState()

def f_temperature_value(port):
	t1 = temperature_value.TemperatureValue(port)
	return t1.getTemp()

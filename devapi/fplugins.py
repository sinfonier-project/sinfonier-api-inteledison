import sys

sys.path.append("/opt/tornado")
from plugins import (switch_on_led,temperature_value,screen_control,button_status,light_value)

def f_switch_on_led(port,state):
	l1 = switch_on_led.SwitchOnLed(port,state)
	return l1.setState()

def f_temperature_value(port):
	t1 = temperature_value.TemperatureValue(port)
	return t1.getTemp()

def f_screen_control(r_color,g_color,b_color,x_cur,y_cur,message):
	s1 = screen_control.ScreenControl(r_color,g_color,b_color,x_cur,y_cur,message)
	return s1.setScreen()

def f_button_status(port):
	b1 = button_status.Button(port)
	return b1.getButtonStatus()

def f_light_value(port):
	l1 = light_value.LightValue(port)
	return l1.getLight()

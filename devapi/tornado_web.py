#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ["Eva Suárez (@evasuarez22)", "Pedro J. Martínez (@pejema44)"]
__copyright__ = "Copyright 2015, Telefonica Cybersecurity"
__maintainer__ = ["Eva Suárez (@evasuarez22)", "Pedro J. artínez (@pejema44)"]
__email__ = ["eva.suarez@11paths.com","pedrojesus.martinez@global.11paths.com"]
__status__ = "Beta"
__version__ = "0.1"

import os
from tornado import ioloop,web,httpserver

import fplugins

def Authorization(access_token):
   try:
      f = open("/opt/config.txt","r")
      lines = f.readlines()
      for li in lines: 
	if li.strip() == access_token:
            return True
        else:
            print "Unauthorized, you must introduce the right access_token"
            return False
      f.close()
   except Exception, ex:
      print "config.txt apiconfig file not found. " + str(ex)
      return False

class SwitchOnLed(web.RequestHandler):
	def post(self):
		if Authorization(self.get_argument("access_token", default=0)):
        		a = self.get_argument("port", default = 0)
        		b = self.get_argument("state", default = 0)
        		self.write(fplugins.f_switch_on_led(a, b))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class TemperatureValue(web.RequestHandler):
	def get(self, param):
        	if Authorization(self.get_argument("access_token", default=0)):
			self.write(fplugins.f_temperature_value(param))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class ButtonStatus(web.RequestHandler):	
	def get(self, param):
		if Authorization(self.get_argument("access_token", default=0)):
			self.write(fplugins.f_button_status(param))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class ScreenControl(web.RequestHandler):
	def post(self):
		if Authorization(self.get_argument("access_token", default=0)):
			r = self.get_argument("r_color",default = 255)
			g = self.get_argument("g_color",default = 255)
			b = self.get_argument("b_color",default = 0)
			x = self.get_argument("x_cor",default = 0)
			y = self.get_argument("y_cor",default = 0)
			message = self.get_argument("message",default="default")
			self.write(fplugins.f_screen_control(r, g, b, x, y, message))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class LightValue(web.RequestHandler):
        def get(self, param):
		if Authorization(self.get_argument("access_token", default=0)):
                	self.write(fplugins.f_light_value(param))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class SwitchBuzzer(web.RequestHandler):
        def post(self):
		if Authorization(self.get_argument("access_token", default=0)):
                	a = self.get_argument("port", default = 0)
                	b = self.get_argument("state", default = 0)
			c = self.get_argument("duration", default = 2)
                	self.write(fplugins.f_switch_buzzer_led(a, b, c))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class SoundValue(web.RequestHandler):
        def get(self, param):
		if Authorization(self.get_argument("access_token", default=0)):                
			self.write(fplugins.f_sound_value(param))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class TouchStatus(web.RequestHandler):
        def get(self, param):
		if Authorization(self.get_argument("access_token", default=0)):
                	self.write(fplugins.f_touch_status(param))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

class RotaryAngleValue(web.RequestHandler):
        def get(self, param):
		if Authorization(self.get_argument("access_token", default=0)):
                	self.write(fplugins.f_rotary_angle_value(param))
		else:
			self.write("<p>HTTP 401: Unauthorized</p> <p>Check if your token is correct</p>")

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), 
"templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : False  #Put on false for multiple sub-processes 
}
 
application = web.Application([
    #(r'/static/(.*)', web.StaticFileHandler, {"path": "./static"},),    
    (r'/api/switchled', SwitchOnLed),
    (r'/api/screen', ScreenControl),
    (r'/api/temperature/(.*)', TemperatureValue),
    (r'/api/button/(.*)', ButtonStatus),
    (r'/api/light/(.*)', LightValue),
    (r'/api/switchbuzzer', SwitchBuzzer),
    (r'/api/sound/(.*)', SoundValue),
    (r'/api/touchsensor/(.*)',TouchStatus),
    (r'/api/rotaryangle/(.*)', RotaryAngleValue)

],**settings)
 
if __name__ == "__main__":   
    server = httpserver.HTTPServer(application)
    server.bind(8888)
    print "Tornado IntelEdison API has Started"    
    server.start(2)
    ioloop.IOLoop.instance().start()

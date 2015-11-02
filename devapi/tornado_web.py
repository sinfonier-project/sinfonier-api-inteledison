#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado import ioloop,web,httpserver

import fplugins


class SwitchOnLed(web.RequestHandler):
	def post(self):
        	a = self.get_argument("port", default = 0)
        	b = self.get_argument("state", default = 0)
        	self.write(fplugins.f_switch_on_led(a, b))

class TemperatureValue(web.RequestHandler):
	def get(self, param):
        	self.write(fplugins.f_temperature_value(param))

class ButtonStatus(web.RequestHandler):
	def get(self, param):
		self.write(fplugins.f_button_status(param))

class ScreenControl(web.RequestHandler):
	def post(self):
		r = self.get_argument("r_color",default = 255)
		g = self.get_argument("g_color",default = 255)
		b = self.get_argument("b_color",default = 0)
		x = self.get_argument("x_cor",default = 0)
		y = self.get_argument("y_cor",default = 0)
		message = self.get_argument("message",default="default")
		self.write(fplugins.f_screen_control(r, g, b, x, y, message))

class LightValue(web.RequestHandler):
        def get(self, param):
                self.write(fplugins.f_light_value(param))

class SwitchBuzzer(web.RequestHandler):
        def post(self):
                a = self.get_argument("port", default = 0)
                b = self.get_argument("state", default = 0)
		c = self.get_argument("duration", default = 2)
                self.write(fplugins.f_switch_buzzer_led(a, b, c))

class SoundValue(web.RequestHandler):
        def get(self, param):
                self.write(fplugins.f_sound_value(param))

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
    (r'/api/sound/(.*)', SoundValue)

],**settings)
 
if __name__ == "__main__":   
    server = httpserver.HTTPServer(application)
    server.bind(8888)
    server.start(2) 
    ioloop.IOLoop.instance().start()

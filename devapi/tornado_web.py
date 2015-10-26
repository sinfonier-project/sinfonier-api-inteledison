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

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), 
"templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : False  #Put on false for multiple sub-processes 
}
 
application = web.Application([
    #(r'/static/(.*)', web.StaticFileHandler, {"path": "./static"},),
    
    (r'/api/switchled', SwitchOnLed),
    (r'/api/temperature/(.*)', TemperatureValue)

],**settings)
 
if __name__ == "__main__":   
    server = httpserver.HTTPServer(application)
    server.bind(8888)
    server.start(2) 
    ioloop.IOLoop.instance().start()

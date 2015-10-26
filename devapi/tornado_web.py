#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado import ioloop,web,httpserver

import fplugins


class SwitchOnLed(web.RequestHandler):
    def get(self, param):
        a = self.get_argument("port", default = 0)
        b = self.get_argument("state", default = 0)
        self.write(fplugins.f_switch_on_led(a, b))


settings = {
    "template_path": os.path.join(os.path.dirname(__file__), 
"templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : False  #Put on false for multiple sub-processes in Pro
}
 
application = web.Application([
    #(r'/static/(.*)', web.StaticFileHandler, {"path": "./static"},),
    
    (r'/api/switchled', SwitchOnLed)

],**settings)
 
if __name__ == "__main__":   
    server = httpserver.HTTPServer(application)
    server.bind(8888)
    server.start(2) #Forks multiple sub-processes Poner a 20 en 
produccion
    ioloop.IOLoop.instance().start()

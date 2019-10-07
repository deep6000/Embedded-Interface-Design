#!/usr/bin/python3

import sys
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
import threading 

# import temperature sensor module
import th_display

class WSHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print ('Hey there, newbie')
		
	def on_message(self, message):
		print ('message received: %s' % message)
		self.write_message(str(message_handler(message)))
		
	def on_close(self):
		print ('connection closed')
		
	def check_origin(self, origin):
		return True
		
application = tornado.web.Application([(r'/ws', WSHandler),])

def message_handler(message):
	if message == "CurrSensVal":
		th = th_display.display()
		humidity, temperature, time  = th.sensor_read()
		if humidity is None or temperature is None:
			return message + str(time) + '+' + "Error + Error"
		
		return message + '+'+ str(time) + '+' + '{0:0.1f}'.format(temperature) + '+' + '{0:0.1f}'.format(humidity)
	
if __name__ == "__main__":
	#x = threading.Thread(target = tornado_func)
	app=QApplication(sys.argv)
	application = tornado.web.Application([(r'/ws', WSHandler),])
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	myIP = "matokor.local"
	print ('---Websocket Server Started at %s---' % myIP)
	tornado.ioloop.IOLoop.instance().start()
	

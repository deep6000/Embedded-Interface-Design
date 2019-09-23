#!/usr/bin/python3

import sys
import datetime
import time
import Adafruit_DHT
import numpy as np

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
count = 0

# temperature and humidity thresholds
th_temperature = 30
th_humidity = 30

class display(QDialog):
	def __init__(self):
		super(display, self).__init__()
		loadUi('th_display.ui',self)
		date = datetime.datetime.now().strftime("%m - %d - %y")
		self.lcd_date.display(str(date))
		self.push_refresh.clicked.connect(self.refresh_display)
		self.push_th_t.clicked.connect(self.set_temperature_threshold)
		self.push_th_h.clicked.connect(self.set_humidity_threshold)
		
		self.push_tempgraph.clicked.connect(self.temperature_graph)
		self.push_stop.clicked.connect(self.terminate)
		# self.push_humgraph.clicked.connect(self.humidity_graph)
		
		# initialize timer to go off every 15s
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.timer_callback)
		self.timer.start(1000)
		
	def set_temperature_threshold(self):
		global th_temperature
		th_temperature = float(self.text_alarm_t.toPlainText())
		
	def set_humidity_threshold(self):
		global th_humidity
		th_humidity = float(self.text_alarm_h.toPlainText())
		
	def sensor_read(self):
	# read sensor values
		global th_temperature, th_humidity
		self.text_t = ""
		self.text_h = ""
		self.humidity, self.temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
		self.time = datetime.datetime.now().strftime("%H:%M:%S")
		
		if self.temperature is None or self.humidity is None:
			return self.humidity, self.temperature, self.time

		if self.temperature > th_temperature:
			self.text_t = "Temperature above threshold"
			
		if self.humidity > th_humidity:
			self.text_h = "\nHumidity above threshold"
			
		self.text_alert.setText( str(self.text_t) + str(self.text_h))
		
		return self.humidity, self.temperature, self.time
		
	def timer_callback(self):
		global count 
		count = count + 1
		#if count > 30:
			# self.terminate()
			
		self.status_line()
		
	def refresh_display(self):
		humidity, temperature, time = self.sensor_read()
		self.lcd_timestamp.display(str(time))
		
		if self.humidity is None or self.temperature is None:
			self.lcd_temperature.display('ERROR')
			self.lcd_humidity.display('ERROR')
			return
		
		self.lcd_temperature.display(temperature)
		self.lcd_humidity.display(humidity)
		
	def status_line(self):
	# read sensor values and return string to dsiplay on the status line
		humidity, temperature, time = self.sensor_read()
		
		if humidity is None or temperature is None:
			self.text_statusline.setText('ERROR! Sensor not connected')
			return
			
		self.text_statusline.setText('['+ str(time)+ ']'+ \
			'\t\tSensor Status: Connected' + '\t\tTemperature: {0:0.1f} C'.format(temperature) \
			+ '\t\tHumidity: {0:0.1f} %'.format(humidity))
		
	def temperature_graph(self):
	# display a graph of past 10 temperature values
	
		# test
		t = np.linspace(0, 1, 10)
		x = np.linspace(0, 1, 10)
		self.matplot_widget.canvas.axes.clear()
		self.matplot_widget.canvas.axes.plot(t, x)
		self.matplot_widget.canvas.axes.legend('sample', 'sample2') 
		self.matplot_widget.canvas.draw()
		
	def terminate(self):
		sys.exit(app.exec_())
		
		  
		
app=QApplication(sys.argv)
widget=display()
widget.show()
widget.terminate()

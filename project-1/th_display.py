#!/usr/bin/python3

import sys
import datetime
import time
import Adafruit_DHT
import numpy as np
import MySQLdb
from MySQLdb import Error
import database

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from database import db_sql

__author__ = "Madhumitha Tolakanhalli , Deepesh Sonigra"
__copyright__ = "Copyright 2019, Temperature -Humidity UI & database"
__email__ = "mato2277@colorado.edu , deso6761@colorado.edu"
__version__ = 1.0
__status__ = "Prototype"


# Sensor Type 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
count = 0

#MYSQL connection parameters
DB_HOSTNAME = 'localhost'
DB_USERNAME = 'pi'
DB_PASSWORD = 'mdp6kor'
DB_NAME     = 'DHT22'
TB_TEMP     = 'DHT22_Temp'
TB_HUMID    = 'DHT22_Humidity'

# temperature and humidity thresholds
th_temperature_c = 30
th_temperature_f = 86
th_humidity = 30
is_farenheit = 0

#create cursor to the database
# Connect to the database
dbase = MySQLdb.connect(
		host=DB_HOSTNAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		)
cursor = dbase.cursor()

#class Display
class display(QDialog):
	def __init__(self):
		super(display, self).__init__()
		loadUi('th_display.ui',self)
		date = datetime.datetime.now().strftime("%m - %d - %y")
		self.lcd_date.display(str(date))
		self.push_refresh.clicked.connect(self.refresh_display)
		self.push_th_t.clicked.connect(self.set_temperature_threshold)
		self.push_th_h.clicked.connect(self.set_humidity_threshold)
		self.push_c_f.clicked.connect(self.toggle_temperature_unit)
		self.push_tempgraph.clicked.connect(self.temperature_graph)
		self.push_stop.clicked.connect(self.terminate)
		self.push_humgraph.clicked.connect(self.humidity_graph)
		self.status_line_init()
		# initialize timer to go off every 15s
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.timer_callback)
		self.timer.start(15000)
		#initialize init values for temperature and humidity threshold
		self.text_alarm_t.setText(str(th_temperature_c))
		self.text_alarm_h.setText(str(th_humidity))

# toggle betwween c & F			
	def toggle_temperature_unit(self):
		global is_farenheit, th_temperature_c, th_temperature_f
		is_farenheit ^= 1
		self.status_line()
		
		if is_farenheit is 1:
			self.text_alarm_t.setText("%0.2f"%th_temperature_f)
		else:
			self.text_alarm_t.setText("%0.2f"%th_temperature_c)
			
		self.refresh_display()
		
#set temperature threshold
	def set_temperature_threshold(self):
		global th_temperature_c, th_temperature_f
		
		if is_farenheit is 1:
			th_temp = float(self.text_alarm_t.toPlainText())
			th_temperature_f = th_temp
			th_temperature_c = (th_temp - 32)*(5/9)
		else:
			th_temp = float(self.text_alarm_t.toPlainText())
			th_temperature_c = th_temp
			th_temperature_f = (th_temp * 1.8 + 32)
			
	def set_humidity_threshold(self):
		global th_humidity
		th_humidity = float(self.text_alarm_h.toPlainText())

# Sensor read values 		
	def sensor_read(self):
	# read sensor values
		global th_temperature_f, th_temperature_c, th_humidity
		
		self.text_t = ""
		self.text_h = ""
		self.humidity, self.temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
		self.time = datetime.datetime.now().strftime("%H:%M:%S")
		
		if self.temperature is None or self.humidity is None:
			return self.humidity, self.temperature, self.time

		if is_farenheit is 1:
			if (self.temperature * 1.8 + 32) > th_temperature_f:
				self.text_t = ("Temperature above Threshold Value %0.2f"%th_temperature_f)
		else:
			if self.temperature > th_temperature_c:
				self.text_t = ("Temperature above Threshold Value %0.2f"%th_temperature_c)
			
		if self.humidity > th_humidity:
			self.text_h = ("\nHumidity above hreshold Value %0.2f"%th_humidity)
			
		self.text_alert.setText( str(self.text_t) + str(self.text_h))
		
		return self.humidity, self.temperature, self.time

# timer callback function
	def timer_callback(self):
		global count 
		count = count + 1
		if count > 30:
			self.terminate()
		self.status_line()

# refresh display
	def refresh_display(self):
		humidity, temperature, time = self.sensor_read()
		self.lcd_timestamp.display(str(time))
		
		if self.humidity is None or self.temperature is None:
			self.lcd_temperature.display('ERROR')
			self.lcd_humidity.display('ERROR')
			return
		
		if is_farenheit is 1:
			temperature = temperature * 1.8 + 32
			self.lcd_temperature.display(temperature)
			self.label_t_unit.setText("Farenheit")
			self.lcd_humidity.display(humidity)
		else:
			self.lcd_temperature.display(temperature)
			self.lcd_humidity.display(humidity)
			self.label_t_unit.setText("Celcius")
	
	def status_line_init(self):
		# read sensor values and return string to dsiplay on the status line
		humidity, temperature, time = self.sensor_read()
		
		if humidity is None or temperature is None:
			self.text_statusline.setText('ERROR! Sensor not connected')
			return
		
		if is_farenheit is 1:
			temperature = temperature * 1.8 + 32
			self.text_statusline.setText('['+ str(time)+ ']'+ \
				'\t\tSensor Status: Connected' + '\t\tTemperature: {0:0.1f} F'.format(temperature) \
				+ '\t\tHumidity: {0:0.1f} %'.format(humidity))
		else:
			self.text_statusline.setText('['+ str(time)+ ']'+ \
				'\t\tSensor Status: Connected' + '\t\tTemperature: {0:0.1f} C'.format(temperature) \
				+ '\t\tHumidity: {0:0.1f} %'.format(humidity))

#status line function		
	def status_line(self):
		# read sensor values and return string to dsiplay on the status line
		humidity, temperature, time = self.sensor_read()
		
		if humidity is None or temperature is None:
			self.text_statusline.setText('ERROR! Sensor not connected')
			return
			
		db = database.db_sql()
		db.load_temp_val(cursor, temperature)
		db.load_humidity_val(cursor, humidity)
		db.commit_db(dbase)
			
		if is_farenheit is 1:
			temperature_f = temperature * 1.8 + 32
			self.text_statusline.setText('['+ str(time)+ ']'+ \
				'\t\tSensor Status: Connected' + '\t\tTemperature: {0:0.1f} F'.format(temperature_f) \
				+ '\t\tHumidity: {0:0.1f} %'.format(humidity))
		else:
			self.text_statusline.setText('['+ str(time)+ ']'+ \
				'\t\tSensor Status: Connected' + '\t\tTemperature: {0:0.1f} C'.format(temperature) \
				+ '\t\tHumidity: {0:0.1f} %'.format(humidity))

# Celcuis to farenheit conversion
	def Celcuis2Farenheit(self, db_t):
		db_tf = [((db_t[i]*(9/5)) + 32) for i in range(len(db_t))]
		return db_tf

# Temperature graph function
	def temperature_graph(self):
	# display a graph of past 10 temperature values
		db = database.db_sql()
		x = np.linspace(0, 1, 10)
		t = db.read_last_n_records(cursor, TB_TEMP, 10)
		
		if is_farenheit is 1:
				t = self.Celcuis2Farenheit(t)
	
		self.matplot_widget.canvas.axes.clear()
		self.matplot_widget.canvas.axes.plot(x, t)
		self.matplot_widget.canvas.axes.legend('Readings', 'Temperature') 
		self.matplot_widget.canvas.draw()
		
# humidity graph function		
	def humidity_graph(self):
	# display a graph of past 10 humidity values
		x = np.linspace(0, 1, 10)
		db = database.db_sql()
		t = db.read_last_n_records(cursor, TB_HUMID, 10)
		self.matplot_widget.canvas.axes.clear()
		self.matplot_widget.canvas.axes.plot(x, t)
		self.matplot_widget.canvas.axes.legend('Readings', 'Humidity') 
		self.matplot_widget.canvas.draw()
		
	def terminate(self):
		sys.exit(app.exec_())
				
if __name__ == "__main__":
	######## MAIN CODE ###########
	app=QApplication(sys.argv)
	widget=display()
	#create database 
	db_obj = database.db_sql()
	db_obj.create_database(cursor,DB_NAME)
	#select the database
	db_obj.use_database(cursor,DB_NAME)
	#create temperature Table
	db_obj.create_temp_tb(cursor)
	#create Humidity table
	db_obj.create_humidity_tb(cursor)
	# commit the changes
	db_obj.commit_db(dbase)
	widget.show()
	widget.terminate()


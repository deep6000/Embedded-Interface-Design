#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from picamera import PiCamera
from time import sleep
import pyaudio
import numpy as np


chunk=4096
RATE=44100

class Client(QWidget):
	camera = PiCamera()
	def __init__(self):
		super().__init__()

	def main(self):
		Client.camera.resolution = (640, 480)
		Client.camera.start_preview()
		sleep(5)
		Client.camera.capture('image.jpg')
		Client.camera.stop_preview()
		
		# Widget
		self.setWindowTitle("Captured Image")
		self.setGeometry(10, 10, 640, 480)
		label = QLabel(self)
		pixmap = QPixmap('image.jpg')
		label.setPixmap(pixmap)
		self.show()
		#The following code comes from markjay4k as referenced below
		p=pyaudio.PyAudio()

		#input stream setup
		stream=p.open(format = pyaudio.paInt16,rate=RATE,channels=1, input_device_index = 2, input=True, frames_per_buffer=chunk)

		#the code below is from the pyAudio library documentation referenced below
		#output stream setup
		player=p.open(format = pyaudio.paInt16,rate=RATE,channels=1, output=True, frames_per_buffer=chunk)

		while True:            #Used to continuously stream audio
			 data=np.fromstring(stream.read(chunk,exception_on_overflow = False),dtype=np.int16)
			 player.write(data,chunk)
			
		#closes streams
		stream.stop_stream()
		stream.close()
		p.terminate
		sys.exit(app.exec_())
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	obj = Client()
	obj.main()



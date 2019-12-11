#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from picamera import PiCamera
from time import sleep
import numpy as np
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from tempfile import gettempdir
from contextlib import closing
import subprocess
import os
from pygame import mixer
import pyaudio
import wave
import boto3
from time import sleep
import requests

chunk=4096
RATE=44100

bucket_wave="buckwave"
bucket_image="buckimg"
region="us-east-1"
capture= "image.jpg"
Confidence = 80
audio_file = "speech.mp3"
command_filename = 'identify.wav' # name of .wav file
feedback_filename = 'feedback.wav' # name of .wav file
identify_command = "identify"
right_feedback = "Right"
wrong_feedback = "Wrong"

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 48000 # 48kHz sampling rate
chunk = 2 # 2^12 samples for buffer
record_time = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file


audio = pyaudio.PyAudio() # create pyaudio instantiation




class Client(QWidget):
	camera = PiCamera()
	
	def __init__(self):
		super().__init__()
	"""
	Initialize the display
	"""
	def main(self):
		Client.camera.resolution = (640, 480)
		# Widget
		self.setWindowTitle("Captured Image")
		self.setGeometry(10, 10, 640, 480)
		label = QLabel(self)
		pixmap = QPixmap('image.jpg')
		label.setPixmap(pixmap)
		self.show()
	
	"""
	Capture the image
	image is the file name of the image;
	return object of the image
	"""	
	def capture_image(image ):
		Client.camera.capture(image)
		return image
	
	"""
	Upload the content to the specified bucket
	"""		
	def upload_to_bucket(content,bucket):
		S3 = boto3.client('s3')
		S3.upload_file(content,bucket,content) 
	
	"""
	Detect the labels for specified image in the specified bucket
	returm the label with max confidence 
	"""	
	def detect_img_labels(image,bucket):
		confidence= 0
		client=boto3.client('rekognition',region)
		print("Recognizing")
		response = client.detect_labels(
					Image={
							'S3Object':{
									'Bucket':bucket,'Name':image
									}
							},
									MaxLabels=10)
		
			 
		for i in response['Labels']:
			if (confidence < i['Confidence']):
					confidence = i['Confidence']
					label = i['Name']
		
		return label
	
	"""
	 Convert the text passed into a speech file specified 
	"""	
	
	def text_to_speech(text,speech_file):
		polly_client = boto3.client('polly',region)
		try:
			response = polly_client.synthesize_speech(VoiceId='Joanna',
			OutputFormat='mp3', 
			Text = text)
		except (BotoCoreError, ClientError) as error:
			print(error)
			sys.exit(-1)
		file = open(speech_file, 'wb')
		file.write(response['AudioStream'].read())
		file.close()
	
	"""
	record audio for given number of seconds 
	"""	
	def record_audio(wav_output_filename,record_secs):
		# create pyaudio stream
		stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
		print("recording")
		frames = []

		# loop through stream and append audio chunks to frame array
		for i in range(0,int((samp_rate/chunk)*record_secs)):
			data = stream.read(chunk,exception_on_overflow = False)
			if i % 3 == 0:
				frames.append(data)

		print("finished recording")
		# stop the stream, close it, and terminate the pyaudio instantiation
		stream.stop_stream()
		stream.close()
		
		
		# save the audio frames as .wav file
		wavefile = wave.open(wav_output_filename,'wb')
		wavefile.setnchannels(chans)
		wavefile.setsampwidth(audio.get_sample_size(form_1))
		wavefile.setframerate(samp_rate/3)
		wavefile.writeframes(b''.join(frames))
		wavefile.close()
	
	"""
	play audio for given input file
	"""	
		
	def play_audio(input_file):
		mixer.music.load(audio_file)
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
		mixer.music.stop()
	
	"""
	using lex bot to convert speech to text of given input wave file
	"""	
	def aws_lex(wavefile):
		
		lex_run = boto3.client('lex-runtime', region_name = region)
		wavefile = wave.open(wavefile)
		response = lex_run.post_content(botName = "texttospeech", 
										botAlias = "command", 
										contentType = "audio/l16;rate=16000; channels=1",
										accept = "text/plain; charset=utf-8",\
										inputStream = wavefile.readframes(96044), userId = "test")
										
		text_data = response['ResponseMetadata']['HTTPHeaders']['x-amz-lex-message']
		return text_data
	
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	obj = Client()
	obj.main()
	feedback_done = 0;
	print("Record AUDIO")
	Client.record_audio(command_filename,3)
	command = Client.aws_lex(command_filename)
	
	if identify_command in command:
		mixer.init()
		#Client.camera.start_preview()
		#sleep(5)
		capture = Client.capture_image(capture)
		#Client.camera.stop_preview()
		Client.upload_to_bucket(capture,bucket_image)
		captured_label = Client.detect_img_labels(capture,bucket_image)
		print(captured_label)
		
		if captured_label is not None:
			Client.text_to_speech(captured_label,audio_file)
			Client.play_audio(audio_file)
		while feedback_done == 0:
			print("Give Feedback")
			Client.record_audio(feedback_filename,3)
			command = Client.aws_lex(feedback_filename)
			print(command)
			if right_feedback in command:
				print("Rightly detected object")
				feedback_done = 1
			elif wrong_feedback in command:
				print("Wrongly Detected Object")
				feedback_done = 1
			else:
				feedback_done = 0;
	else:
		print("retry recording audio")
	
	sys.exit(app.exec_())

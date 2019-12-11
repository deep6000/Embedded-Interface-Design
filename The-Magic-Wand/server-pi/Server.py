#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QTableWidgetItem
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from serverGUI import *
import sys
import boto3
import database
import MySQLdb
from MySQLdb import Error
import datetime

_author__ = "Madhumitha Tolakanhalli , Deepesh Sonigra"
__copyright__ = "Copyright 2019, Magic Wand"
__email__ = "mato2277@colorado.edu , deso6761@colorado.edu"
__version__ = 1.0
__status__ = "Prototype"

#MYSQL connection parameters
DB_HOSTNAME = 'localhost'
DB_USERNAME = 'pi'
DB_PASSWORD = 'mdp6kor'
DB_NAME     = 'Magic_Wand'



#create cursor to the database
# Connect to the database
dbase = MySQLdb.connect(
		host=DB_HOSTNAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		)
cursor = dbase.cursor()


#region AWS
region="us-east-1"

# Bucket to store image
bucket_image="buckimg"
# Name of the image stored on the cloud
image_on_cloud = "image.jpg"
# Name of downloaded image from the bucket
image_on_pi = "image_local.jpg"

#SQS queue link
myQueueUrl='https://sqs.us-east-1.amazonaws.com/750237606151/thatpithingqueue'

class Server(QMainWindow, QLabel):
	def __init__(self):
		super().__init__()
		loadUi('serverGUI.ui',self)
		self.tableWidget.setHorizontalHeaderLabels(('TIMESTAMP', 'DETECTED OBJECT', 'RIGHT/WRONG'))
		self.push_refresh.clicked.connect(self.refresh)
		self.push_close.clicked.connect(self.terminate)
		self.push_stats.clicked.connect(self.statistics)
		
	def terminate(self):
		sys.exit(app.exec())
		
	def refresh(self):
		s3 = boto3.client('s3')
		obj = database.db_sql()
		s3.download_file(bucket_image, image_on_cloud, image_on_pi)
		self.label_img.setPixmap(QtGui.QPixmap(image_on_pi))
		Label,Feedback = obj.get_last_record(cursor)
		
		self.label_recog.setText(Label)
		self.label_rw.setText(Feedback)
		
		
		
	def statistics(self):
		obj = database.db_sql()
		obj_percentage = obj.get_right_percentage(cursor)
		command_percentage = obj.get_command_percentage(cursor)

		#set percentage to string
		self.label_obj.setText(str(obj_percentage))
		self.label_cmd.setText(str(command_percentage))
		data = []
		readings = obj.read_last_n_records(cursor,5)
		for rows in  readings:
			data.append(tuple(rows))
		
		row = 0
		for tup in data:
			col = 0
			for item in tup:
				cellinfo = QTableWidgetItem(item)
				self.tableWidget.setItem(row, col, cellinfo)
				col+=1
			row +=1
		print("STATS")
		
if __name__ == "__main__":
	app = QApplication([])
	db_obj = database.db_sql()
	db_obj.use_database(cursor,DB_NAME)
	db_obj.show_tables(cursor);
	widget = Server()
	widget.show()
	widget.terminate()
		
		

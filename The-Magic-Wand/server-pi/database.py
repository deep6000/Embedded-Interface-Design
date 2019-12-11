#!/usr/bin/python3
import MySQLdb
from MySQLdb import Error
import datetime

class db_sql():
	#connect to mysql
	def connect_to_mysql(self, hostname, username, password):
		db = MySQLdb.connect(
		host=hostname,
		user=username,
		passwd=password,
		)
		return db

	#create database
	def create_database(self, cursor,db_name):
		command = ("CREATE DATABASE IF NOT EXISTS %s" % db_name)
		cursor.execute(command)

	#Select the database of the name db_name
	def use_database(self, cursor,db_name):
		command= ("USE %s" %db_name)
		cursor.execute(command)

	def delete_database(self, cursor, db_name):
		command = ("DROP DATABASE %s"%db_name)


	#show all tables in the list
	def show_tables(self, cursor):
		cursor.execute("SHOW TABLES")
		for x in cursor:
			print(x)
			

	#commiting changes to the database
	def commit_db(self, db):
		db.commit()

	#delete the table with name tb_name
	def delete_table(self, cursor,tb_name):
		command = ("DROP TABLE IF EXISTS %s" % tb_name)
		cursor.execute(command)

	#get current time
	def get_timestamp(self):
		ts = datetime.datetime.now().timestamp()
		return ts


		#get the percentage of rightly detected command
	def get_command_percentage(self, cursor):
		command ="select * from Command_Table"
		recognized = 0
		total = 0
		percentage = 0
		cursor.execute(command)
		readings = cursor.fetchall()
		for row in readings:
			if row [2] == "Recognized":
				recognized = recognized + 1
			total = total + 1
		if  total == 0:
			total = 1
		percentage = (recognized * 100)/total
		return percentage	

	#get the percentage of rightly detected objects
	def get_right_percentage(self, cursor):
		right = 0
		total = 0
		percentage = 0
		command ="select * from Label_Table"
		cursor.execute(command)
		readings = cursor.fetchall()
		for row in readings:
			if row [3] == "Right":
				right = right + 1
			total = total + 1
		if  total == 0:
			total = 1
		percentage = (right * 100)/total
		return percentage


	def get_last_record(self,cursor):
		command = ("select * from Label_Table ORDER BY SerialNo DESC LIMIT 1;")
		cursor.execute(command)
		readings = cursor.fetchall()
		for rows in readings:
			return rows[2], rows[3]
			

	#read the last n records of particulat table
	def read_last_n_records(self,cursor,count):
		command = ("select timestamp,Label,Feedback from Label_Table ORDER by SerialNo DESC LIMIT %d" %(count))
		cursor.execute(command)
		readings = cursor.fetchall()
		return readings
	


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
	#create temperature table
	def create_temp_tb(self, cursor):
		cursor.execute("CREATE TABLE IF NOT EXISTS DHT22_Temp (serialNo INT AUTO_INCREMENT PRIMARY KEY, timestamp BIGINT NOT NULL, value FLOAT)")

	#create humidity table
	def create_humidity_tb(self, cursor):
		cursor.execute("CREATE TABLE IF NOT EXISTS DHT22_Humidity (serialNo INT AUTO_INCREMENT PRIMARY KEY, timestamp BIGINT NOT NULL , value FLOAT)")

	#show all tables in the list
	def show_tables(self, cursor):
		cursor.execute("SHOW TABLES")
		for x in cursor:
			print(x)
			
	#insert temperature reading in temperature table
	def insert_temp_value(self, cursor,timestamp,temp_val):
	   command = ("INSERT INTO DHT22_Temp (timestamp,value) VALUES (%s,%s)")
	   val = (timestamp, temp_val)
	   cursor.execute(command,val)

	#insert humidity reading in humidity table
	def insert_humidity_value(self, cursor,timestamp,humid_val):
		command = ("INSERT INTO DHT22_Humidity (timestamp,value) VALUES (%s,%s)")
		val = (timestamp, humid_val)
		cursor.execute(command,val)
	   
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

	#load current value of temperature in the database along with timestamp
	def load_temp_val(self, cursor,temp_val):
		ts = self.get_timestamp()
		self.insert_temp_value(cursor,ts,temp_val);

	#load humidity value in database along with timestamp
	def load_humidity_val(self, cursor,humid_val):
		ts = self.get_timestamp()
		self.insert_humidity_value(cursor,ts,humid_val);

	#read the entire temperature table
	def read_tb_temp(self, cursor):
		command ="select * from DHT22_Temp"
		cursor.execute(command)
		readings = cursor.fetchall()
		for row in readings:
			print("|SerialNo = %d | Timestamp = %ld | Value = %f" %(row[0], row[1], row[2]))

	#read the entire humidity table
	def read_tb_humid(self, cursor):
		command ="select * from DHT22_Humidity"
		cursor.execute(command)
		readings = cursor.fetchall()
		for row in readings:
			print("|SerialNo = %d | Timestamp = %ld | Value = %f" %(row[0], row[1], row[2]))

	#read the last n records of particulat table
	def read_last_n_records(self,cursor, tb_name,count):
		command = ("select * from %s ORDER by SerialNo DESC LIMIT %d" %(tb_name,count))
		cursor.execute(command)
		readings = cursor.fetchall()
		return readings
	

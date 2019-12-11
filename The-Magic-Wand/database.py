#!/usr/bin/python3
import mysql.connector
from MySQLdb import Error
import datetime

DB_HOSTNAME = 'localhost'
DB_USERNAME = 'pi'
DB_PASSWORD = 'mdp6kor'
DB_NAME     = 'Magic_Wand'
TB_COMMAND     = 'Command_Table'
TB_LABEL    = 'Label_Table'

dbase = mysql.connector.connect(
		host=DB_HOSTNAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		)
print(dbase)
cursor = dbase.cursor()
print(cursor)

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
    def create_command_tb(self, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS Command_Table (serialNo INT AUTO_INCREMENT PRIMARY KEY, timestamp BIGINT NOT NULL,Command VARCHAR(30)")

    #create humidity table
    def create_label_tb(self, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS Label_Table (serialNo INT AUTO_INCREMENT PRIMARY KEY, timestamp BIGINT NOT NULL , Label VARCHAR(30), Feeback VARCHAR(30)")

    #show all tables in the list
    def show_tables(self, cursor):
        cursor.execute("SHOW TABLES")
        for x in cursor:
            print(x)
                    
    #insert temperature reading in temperature table
    def insert_command(self, cursor,timestamp,message):
        command = ("INSERT INTO Command_Table (timestamp,Command) VALUES (%s,%s)")
        val = (timestamp, temp_val)
        cursor.execute(command,val)

    #insert humidity reading in humidity table
    def insert_label(self, cursor,timestamp,label,feedback):
        command = ("INSERT INTO Label_Table (timestamp,Label,Feedback) VALUES (%s,%s)")
        val = (timestamp, humid_val)
        cursor.execute(command,val)
       
    #commiting changes to the database
    def commit_db(self, db):
        db.commit()

    #delete the table with name tb_name
    def delete_table(self, cursor,tb_name):
        command = ("DROP TABLE IF EXISTS %s" % tb_name)
        cursor.execute(command)



    #get the percentage of rightly detected command
    def get_command_percentage(self, cursor):
        command ="select * from Command_Table"
        recognized = 0
        total = 0
        cursor.execute(command)
        readings = cursor.fetchall()
        for row in readings:
            if row [1] is "Recognized":
                recognized = recognized + 1
            total = total + 1
        percentage = (recognized * 100)/total
        return percentage	

    #get the percentage of rightly detected objects
    def get_right_percentage(self, cursor):
        right = 0
        total = 0
        command ="select * from Label_Table"
        cursor.execute(command)
        readings = cursor.fetchall()
        for row in readings:
            if row [2] is "Right":
                right = right + 1
            total = total + 1
        percentage = (right * 100)/total
        return percentage


    #read the last n records of particulat table
    def read_last_n_records(self,cursor, tb_name,count):
        command = ("select * from %s ORDER by SerialNo DESC LIMIT %d" %(tb_name,count))
        cursor.execute(command)
        readings = cursor.fetchall()
        return readings
	


if __name__ == "__ main__":
    db_obj = db_sql()
    cursor.execute("CREATE DATABASE TEST")
   # cursor= db_obj.connect_to_sql(DB_HOSTNAME,DB_USERNAME,DB_PASSWORD)
    db_obj.create_database(cursor,DB_NAME)
    db_obj.commit_db(dbase) 
        #select the database
    db_obj.use_database(cursor,DB_NAME)
	#create temperature Table
    db_obj.create_command_tb(cursor)
	#create Humidity table
    db_obj.create_label_tb(cursor)
	# commit the changes
    db_obj.commit_db(dbase) 
    db_obj.show_tables(cursor)
    insert_command(cursor,1,"Recognized")
    insert_command(cursor,2,"Not_Recognized") 



#!/usr/bin/python3
import MySQLdb
from MySQLdb import Error
import datetime

DB_HOSTNAME = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = 'mdp6kor'
DB_NAME     = 'Magic_Wand'
TB_COMMAND  = 'Command_Table'
TB_LABEL    = 'Label_Table'


class db_sql():
    #connect to mysql
    def connect_to_mysql(self, hostname, username, password):
        db = MySQLdb.connect(
            host=hostname,
            user=username,
            passwd=password,
            )

        return db

    
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
	

dbase = MySQLdb.connect(
		host=DB_HOSTNAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		)
cursor = dbase.cursor()
cursor.execute("USE Magic_Wand")
print("Hello")
   # db_obj.commit_db(dbase) 
cursor.execute("SHOW TABLES")
dbase.commit();
   # insert_command(cursor,1,"Recognized")
    #insert_command(cursor,2,"Not_Recognized") 



var mysql = require('mysql');
const util = require('util');

var AWS = require('aws-sdk');

AWS.config.update({region: 'us-east-1'});

var sqs = new AWS.SQS({apiVersion: '2012-11-05'});

var queueURL = "https://sqs.us-east-1.amazonaws.com/750237606151/thatpithingqueue";

var params = {
 AttributeNames: [
    "SentTimestamp"
 ],
 MaxNumberOfMessages: 1,
 MessageAttributeNames: [
    "All"
 ],
 QueueUrl: queueURL,
 VisibilityTimeout: 1,
 WaitTimeSeconds: 0
};


var database =['Magic_Wand'];
var command_tb = ['Command_Table']
var label_tb = ['Label_Table']

var hostname= ['local_host'];
var username= ['pi']
var password= ['mdp6kor']

/**
*  Function to create the database named db_name
*
**/

function create_database(db_name)
{
	
	var sql = "CREATE DATABASE IF NOT EXISTS " + db_name;
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log("Created Database");
  	});
}

function use_database(db_name)
{
	var sql = "USE "+db_name;
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log("Database Selected");
  	});	
}


function create_command_table(tb_name)
{
	
	var sql = " CREATE TABLE IF NOT EXISTS Command_Table (serialNo INT AUTO_INCREMENT PRIMARY KEY, timestamp VARCHAR(30), Command VARCHAR(30))"; 
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log("Created Command Table");
  	});
	
}

function create_label_table(tb_name)
{
	
	var sql = " CREATE TABLE IF NOT EXISTS Label_Table (serialNo INT AUTO_INCREMENT PRIMARY KEY, timestamp VARCHAR(30) ,Label VARCHAR(30), Feedback VARCHAR(30))"; 
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log("Created Label Table");
  	});
}	


function get_last_temp()
{
	var sql= ("select * from  DHT22_Temp  ORDER by SerialNo DESC LIMIT 1");
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log(result); 
	return result[0].value;
 	});
	
}


function insert_command_table(timestamp,command)
{
	var sql = "INSERT INTO Command_Table (timestamp,Command) VALUES ('%s', '%s')";
	var sql_query = util.format(sql,timestamp,command);
	console.log(sql_query);
	con.query(sql_query, function (err,result) {
   	if (err) throw err;
    	console.log("Insert Sucess Command Table");
  	});
}


function insert_label_table(timestamp,label,feedback)
{
	var sql = "INSERT INTO Label_Table (timestamp,Label,Feedback) VALUES ( '%s','%s','%s')";
	var sql_query = util.format(sql,timestamp,label,feedback);
	console.log(sql_query);
	con.query(sql_query, function (err,result) {
   	if (err) throw err;
    	console.log("Insert Success Label Table");
  	});
}

/**
* Function to get last n records from the MYSQL database of thr selected table 
*
**/

function get_last_n_records(tb_name,n)
{
	var sql= ("select * from "+tb_name+ " ORDER by SerialNo DESC LIMIT " +n);
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log(result); 
	return result;
 	});
	
}



var con = mysql.createConnection({
    host: "localhost",
    user: "pi",
    password:  "mdp6kor"
});


con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");

 });

create_database(database);
use_database(database);
create_command_table(command_tb);
create_label_table(label_tb);
//insert_command_table();
//insert_label_table(1,label,feedback);

while(1)
{
	sqs.receiveMessage(params, function(err, data) {
				console.log("IN SQS");
				var evtdata;
				if (err) console.log(err, err.stack);
				else if(data.Messages)
				{
				
						var length = data.Messages.length;
						if(length === 0);
							//console.log("Queue Empty");
							
						else{
							//console.log("Data Received");
							evtdata = JSON.parse(JSON.parse(data.Messages[0].Body)); 
							

							// delete the parameter from the Queue
							/**var delparams = { QueueUrl:queueURL, ReceiptHandle: data.Messages[0].ReceiptHandle };
							 sqs.deleteMessage(deleteParams, function(err, data) {
								if (err) {
									console.log("Delete Error", err);
								} else {
									console.log("Message Deleted", data);
      }
    });*/
							if(evtdata.MessageType === "ImgRecog")
								insert_label_table(evtdata.timestamp,evtdata.Label,evtdata.Feedback)
								
							else if(evtdata.MessageType === "CmdRecog")
								insert_command_table(evtdata.timestamp.toString,evtdata.Feedback.toString)	
						}
					}
				
				});
			}
			
con.on('close', function(reasonCode, description) {

console.log('Client has disconnected.');
        });

//con.end((err) => {
  // The connection is terminated gracefully
  // Ensures all previously enqueued queries are still
   //before sending a COM_QUIT packet to the MySQL server.
//})

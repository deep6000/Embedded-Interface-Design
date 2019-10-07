var mysql = require('mysql');
const http = require('http');
const util = require('util');
const WebSocketServer = require('websocket').server;


global.temperature = 0;
global.humidity = 0;
global.timestamp= 0;


const server = http.createServer();
server.listen(9898);


const wsServer = new WebSocketServer({
  	httpServer: server
});


var database =['DHT22'];
var temp_tb = ['DHT22_Temp']
var humid_tb = ['DHT22_Humidity']


/**
*  Function to Select the database named db_name
*
**/
function use_database(db_name)
{
	
	var sql = "USE "+db_name;
	con.query(sql, function (err,result) {
   	if (err) throw err;
    //	console.log("result");
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
    password: "mdp6kor"
  });

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");

 });
		
wsServer.on('request', function(request) {
	const connection = request.accept(null, request.origin);

        connection.on('message', function(message) {
	
	if(message.utf8Data == "TableNodejs"){

	console.log("received TableNodejs");
	use_database(database);
	var sql= ("select * from DHT22_Humidity ORDER by SerialNo DESC LIMIT 10");
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log(result); 
	var json = JSON.stringify(result)
	connection.sendUTF(json);
	});
	}
	else if(message.utf8Data == "CurrDBVal"){

	use_database(database);
	var sql= ("select * from DHT22_Humidity ORDER by SerialNo DESC LIMIT 1");
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log(result); 
	var json = JSON.stringify(result)
	connection.sendUTF(json);
	});	
	}
	else if(message.utf8Data == "HumGraph"){

	use_database(database);
	var sql= ("select * from DHT22_Humidity ORDER by SerialNo DESC LIMIT 10");
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log(result); 
	var json = JSON.stringify(result)
	connection.sendUTF(json);
	});
	}
	
	var sql= ("select * from DHT22_Temp ORDER by SerialNo DESC LIMIT 1");
	con.query(sql, function (err,result) {
   	if (err) throw err;
    	console.log(result); 
	var json = JSON.stringify(result)
	connection.sendUTF(json);
	});
});	       
});



        con.on('close', function(reasonCode, description) {
            console.log('Client has disconnected.');
        });


//con.end((err) => {
  // The connection is terminated gracefully
  // Ensures all previously enqueued queries are still
  // before sending a COM_QUIT packet to the MySQL server.
//});

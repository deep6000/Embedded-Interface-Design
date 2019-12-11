# Embedded-Interface-Design

## Project 6 - The Magic Wand

### Team Members
          - Deepesh Sonigra
          - Madhumitha Tolakanahalli Pradeep

## Description
          The Magic Wand performs as outlined below –
          •	Client PI
              o	The User presses the mic button to enable the mic and says “Identify” using AWS Lex
              o	An Image is captured from the RPi Camera, sent to AWS Rekognition to recognize it and output on the Speaker(using AWS Polly)
              o	The wand waits for the user to confirm if what has been recognized was right / wrong.
              o	The recognized label is sent to AWS Cloud (SQS)

          •	Server Pi
              o	The Server Pi functions mainly as the PyQt UI for statistics and a database that is implemented using Node.js
              o	The user can obtain information about the wand like – last clicked image, accuracy of commands and image recognition

          
## Installation Instructions 
1) Python Installation

          -sudo apt-get update
          -sudo apt-get upgrade
          -sudo apt-get install python3-dev python3-pip
          
          
2) Install Pyqt5
          -sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
          
3) Install Qt
          -sudo apt-get install qttools5-dev-tools
         
4) Install Database Maria DB
          -sudo apt-get install mariadb-server
          -sudo apt-get install libmariadbclient-dev
          -sudo apt-get install python3-mysqldb
          -sudo apt-get install mariadb-client
          
5) Enable Secure Login to the database

          -sudo mysql_secure_installation
          **set root password if not set and select yes for all options for more security
6) Create USER for database 

          - https://tableplus.com/blog/2018/09/mariadb-how-to-create-new-user-and-grant-privileges.html
          
7) Update AWS Credentials each time the Pi is rebooted
 
8) Clone the repository 
          
          - https://github.com/deep6000/Embedded-Interface-Design
          
9) Change the MySQL connection parameters

          You should change the username and passord for the database to above set username and password
          - sudo vi th_display.py
          - Change the parameters under MySQL parameters "DB_USERNAME, DB_PASSWORD" to your mysql username and password
          
 10) Run the executible
         - On the Client and Server Pi, run database.js and then client.py / server.py respectively
 
 ## Project Work
          - Deepesh Sonigra : Database Installation,Creation,MySQL code,QT- Database Intergration,Sensor Integration 
          - Madhumitha Tolakanahalli : QT Environment setup, PYQT5, Matplotlib,Timers, QT- Database Intergration
          
##References

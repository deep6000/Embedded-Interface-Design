# Embedded-Interface-Design

## Project 6 - The Magic Wand

### Team Members
          - Deepesh Sonigra
          - Madhumitha Tolakanahalli Pradeep

## Description
          The Magic Wand performs as outlined below –
          • Client PI
              o The User presses the mic button to enable the mic and says “Identify” using AWS Lex
              o An Image is captured from the RPi Camera, sent to AWS Rekognition to recognize it and output on the Speaker(using AWS Polly)
              o The wand waits for the user to confirm if what has been recognized was right / wrong.
              o The recognized label is sent to AWS Cloud (SQS)

          • Server Pi
              o The Server Pi functions mainly as the PyQt UI for statistics and a database that is implemented using Node.js
              o The user can obtain information about the wand like – last clicked image, accuracy of commands and image recognition

          
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

5) Install NodeJs 
          
          - curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
          - Restart your terminal
          - nvm –version = Should return a version number like 0.34.0
          - nvm install node  = This installs the latest node, 12.9.0
          - nvm install 10.16.3  = This installs the stable LTS 10.16.3 node
          - node -v = If working, returns the version number
          - npm –v If working, returns the version of npm installed with node.js
          - npm install http
          - npm install mysql
          
          Naked
          - pip install Naked

6) Enable Secure Login to the database

          -sudo mysql_secure_installation
          **set root password if not set and select yes for all options for more security
7) Create USER for database 

          - https://tableplus.com/blog/2018/09/mariadb-how-to-create-new-user-and-grant-privileges.html
          
8) Update AWS Credentials each time the Pi is rebooted
 
8) Clone the repository 
          
          - https://github.com/deep6000/Embedded-Interface-Design
          
10) Change the MySQL connection parameters

          You should change the username and passord for the database to above set username and password
          - sudo vi th_display.py
          - Change the parameters under MySQL parameters "DB_USERNAME, DB_PASSWORD" to your mysql username and password
          
 11) Run the executible
         - On the Server Pi, run database.js and then Server.py and Client side client.py respectively
 

##Project Additions
        - QT User Interface on the Client side to see what image was clicked to give feedback
        - Mic Button Interface to allow user to record when required
        - Retries Allowed on wrongly detected commands allowing users to not repeat the process again.

 ## Project Work
          - Deepesh Sonigra : Database Installation,Creation,MySQL code,QT- Database Intergration,Sensor Integration AWS S3 bucket, AWS LEX
          - Madhumitha Tolakanahalli : QT setup, PYQT5,Timers, QT- Database Intergration, AWS SQS, AWS Image Rekognition, AWS POLY, NOdeJS
          
##References
[1] http://www.devengineering.com/blog/testing/run-nodejs-script-python (Python script for NodeJS)
[2] https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html 
[3] https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html (S3 Bucket)
[4] https://stackoverflow.com/questions/48135955/by-installing-pyaudio-python3-on-my-raspberry-pi-3-noobs-i-get-an-error-how (Installing PyAudio)
[5] https://iotbytes.wordpress.com/connect-configure-and-test-usb-microphone-and-speaker-with-raspberry-pi/ (Microphone Interface)

# Embedded-Interface-Design

## Project 1 - Temperature - Humidity Sensor UI and Database

### Team Members
          - Deepesh Sonigra
          - Madhumitha Tolakanahalli

## Installation Instructions 
1) Adafruit DHT22 Sensor Installation[3]

          -sudo python3 -m pip install --upgrade pip setuptools wheel
          -sudo pip3 install Adafruit_DHT
           

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
 
7) Clone the repository 
          
          - https://github.com/deep6000/Embedded-Interface-Design
          
8) Change the MySQL connection parameters

          You should change the username and passord for the database to above set username and password
          - sudo vi th_display.py
          - Change the parameters under MySQL parameters "DB_USERNAME, DB_PASSWORD" to your mysql username and password
 9) Run the executible
         
         -sudo python3 th_display.py    or
         ./th_display.py
 
 ## Project Work
          - Deepesh Sonigra : Database Installation,Creation,MySQL code,QT- Database Intergration,Sensor Integration 
          - Madhumitha Tolakanahalli : QT Environment setup, PYQT5, Matplotlib,Timers, QT- Database Intergration
          
 ## Project Additions
          - A button interface to change the entire display from the Celcius to Farenheit
          - Retention of threshold values of temperature on change of display from Celcius to Farenheit and vice versa 
          - Macros for database name table names and mysql user login details to change names according to user preferences
          - Error handling provided where it creates database and tables if not exists.
        
 ## References
          [1]https://tableplus.com/blog/2018/09/mariadb-how-to-create-new-user-and-grant-privileges.html :Create New User
          [2]https://yapayzekalabs.blogspot.com/2018/11/pyqt5-gui-qt-designer-matplotlib.html :Pyqt5 - matplotlib 
          [3]https://github.com/adafruit/Adafruit_Python_DHT - Sensor github library
          [4]https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/wiring : Wiring of the Sensor 

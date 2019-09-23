# Embedded-Interface-Design

## Project 1 - Temperature - Humidity Sensor UI and Database

### Team Name
          - Deepesh Sonigra
          - Madhumitha Tolakanhalli


## Installation Instructions 
1) Install Pyqt5

          -sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools

2) Install Qt

          -sudo apt-get install qttools5-dev-tools
3) Install Database Maria DB

          -sudo apt-get install mariadb-server
          -sudo apt-get install libmariadbclient-dev
          -sudo apt-get install python3-mysqldb
          -sudo apt-get install mariadb-client
4) Enable Secure Login to the database

          -sudo mysql_secure_installation
           **set root password if not set and select yes for all options for more security
5) Create USER for database 

          - https://tableplus.com/blog/2018/09/mariadb-how-to-create-new-user-and-grant-privileges.html
 
6) Clone the repository 
          
           - https://github.com/deep6000/Embedded-Interface-Design
7) Edit the th_display file 
 
 The databse is set to login using username and password for our raspberry pi.You should change the username 
           - sudo vi th_display.py
           - 
 
 # References
          [1]https://tableplus.com/blog/2018/09/mariadb-how-to-create-new-user-and-grant-privileges.html
          [2]
          [3]
          [4]

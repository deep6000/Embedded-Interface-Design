# Embedded-Interface-Design

## Project 2 - NodeJS and Tornado Websockets servers with HTML client

### Team Members
          - Deepesh Sonigra
          - Madhumitha Tolakanahalli Pradeep

## Description
   The Python app is the Temperature Humidity Sensor GUI which displays Temperature and Humidity values.
   The user interface involves setting up threshold values and getting temperature and humidity graph from the database.
   This project includes added functionality to the Python app to connect to remote HTML client presenting a Web UI
   The python app initializes the NodeJS and Tornado Websockets to listen to the HTTP websockets.
   The WebUI has capability to connect to these websockets based on the IP address and Port number specified.
   THe web UI contains a connect button to connect to the websockets 
   Once Connected the Web UI provides functionality to read the sensor values by pressing a button.
   On button press, the webUI talks to the tornado using sockets and get sensor values through sockets.
   Similarly a functionality to read Temperature and Humidity values from the database is provided using NodeJS websockets
   

          
## Installation Instructions 
### Follow the instructions for setting up the environment for running the application from the previous project -
          
          - link - https://github.com/deep6000/Embedded-Interface-Design/tree/master/project-1
  
  
  1) Install depencencies
          
          NodeJS, nvm , npm
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

  2) Clone the repository

          - git clone https://github.com/deep6000/Embedded-Interface-Design/
          
         
  3) Run the python app on the server side
  
          - ./th_display.py
          
  4) Run the html client on the Host PC(PC and Raspberry Pi should be in same subnet)
          
          - Open the index.html using your favorite browser (Chrome Recommended)
          
  5) Press connect to connect to Tornado and NodeJS websockets
          
  6) Explore all the features
  
 
 ## Project Work
          - Deepesh Sonigra : NodeJs to Database Connection, NodeJS to HTML Client connection, time performance analysis, HTML
                              tables for NodeJS and Torando
          - Madhumitha Tolakanahalli : Tornado and Python app interface, HTML UI Design, Tornado HTML websockets, F-C Display 
                              conversion, Graph for Temperture and Humidity on Web UI
          
 ## Project Additions
 
         - Allowed User to enter IP address and Port number on the Web UI
        
        
 ## References
[1]https://www.geeksforgeeks.org/how-to-convert-json-data-to-a-html-table-using-javascript-jquery/ (JSON to HTML table)
[2]https://canvasjs.com/javascript-charts/json-data-api-ajax-chart/  (Plotting graphs in HtML)
[3]http://www.devengineering.com/blog/testing/run-nodejs-script-python (Python script for NodeJS)

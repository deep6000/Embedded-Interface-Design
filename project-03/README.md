# Embedded-Interface-Design

## Project 3 - AWS IOT Interface

### Team Members
          - Deepesh Sonigra
          - Madhumitha Tolakanahalli Pradeep

## Description 

The python app sends MQTT push to AWS IOT 3 types of messages- DATA, ALERT , ERRO. We have defined a Lambda rule which triggers a lambda function on AWS IOT receive successful. In Lambda function DATA Type message is further send to AWS SQS to store the value in the Queue. The ALert Type message is send to AWS SNS to send messages/emails to the user as notification. We have an HTML client which reads the data from the SQS queue depending on the demand. We can read a single value of "Temperature , Humidtity and Timestamp" or could read the entire queue based on the button pressed. Reading entire queue displays just 20 latest values from the queue and prints it in a form of table. The Queue length button gives user the capability to know the number of items in the queue at particular time. THe Queue Length also updates itself as soon you read from the Queue. 
          
## Installation Instructions 

1) Follow the instructions to install all dependencies shown the following links

          -https://github.com/deep6000/Embedded-Interface-Design/edit/master/project-1/
          -https://github.com/deep6000/Embedded-Interface-Design/edit/master/project-2/
 
 2) AWS Python SDK Installation
 
          -sudo pip3 install AWSIoTPythonSDK
 
 3) Create an AWS account and Rules to Trigger the Lambda function on MQTT message receive.
          
 4) Change the MQTT Configuration Credentials 
         
 5) Run the executible
         
         -sudo python3 th_display.py    or
         ./th_display.py
 
 ## Project Work
          - Deepesh Sonigra : AWS IOT to SQS , Lambda function,Rule for AWS IOT lambda trigger, SQS to HTML
          - Madhumitha Tolakanahalli : Python app to AWS IOT,SNS rule for Lambda function,Lambda function, AWS IOT to SNS, 
          
 ## Project Additions
         
         - Error Handling when sensor not connected sends message alert to user about sensor not connected.
         - The Queue length button gives the current queue length of the AWS SQS.
         - On Queue Message read the queue prints out Queue is empty if there is not element to read.
         - The Queue length autoupdates itself on Queue read be it either single value or whole queue.
   
   ## Project Issues
   
          - AWS SNS message notification is unreliable and can stop working sometimes.
          - As QOS = 0, we would receive messages multiple times and there won't be any synchronization.
          - Can't Delete messages unless reading it, thus ading overhead
        
 ## References
 [1] https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html AWS Starter Guide
 [2]https://techblog.calvinboey.com/raspberrypi-aws-iot-python/ Streaming sensor data to AWS IOT
 [3] https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html- Getting Started Browser Script.
 [4]https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html Using Lambda with SNS
 [5] https://startupnextdoor.com/adding-to-sqs-queue-using-aws-lambda-and-a-serverless-api-endpoint/ Using Lambda with SQS

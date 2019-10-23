from __future__ import print_function
  
import json
import boto3
  
print('Loading function')

myQueueUrl='https://sqs.us-east-1.amazonaws.com/750237606151/thatpithingqueue'

def lambda_handler(event, context):
  
    eventText = json.dumps(event)
    # Print the parsed JSON message to the console; you can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console
    print('Received event: ', eventText)
    
    data=event
    error = "Error! Sensor disconnected."
    
    # Create an SQS Queue
    sqs = boto3.client('sqs')
    
    
    # Create an SNS client
    sns = boto3.client('sns')
    
    if data['message'] == "Data":
        #send the event to AWS 
        response_sqs = sqs.send_message(
        QueueUrl=myQueueUrl,
        MessageBody=json.dumps(event)
        )
        print("SQS")
    elif data['message'] == "Alert":
        # Send Alert Message as a SMS
        response_sns = sns.publish (
        PhoneNumber = '+17203608545',
        Message = json.dumps(event)
        )
        print("SNS")
    elif data['message'] == "Error":
        #error = "[" + data['timestamp'] + "] " + "Error! Sensor Disconnected"
        # If sensor is disconnected, send SMS with error message
        response_sns = sns.publish (
        TopicArn = 'arn:aws:sns:us-east-1:750237606151:ThatPiSNSTopic',
        Message = json.dumps(event)
        )
        print(response_sns)
        print("Error")
        
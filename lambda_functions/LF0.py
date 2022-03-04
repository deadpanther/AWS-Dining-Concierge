import json
import boto3
import logging

def lambda_handler(event, context):
    
    message = event["messages"][0]['unstructured']['text']
    client = boto3.client('lex-runtime')     
    
    response = client.post_text(
        botAlias='bottest',
        botName='DiningConcierge',
        userId='deadpanther',
        inputText=message)

    return {
        'statusCode': 200,
        'body': response,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        }
    }
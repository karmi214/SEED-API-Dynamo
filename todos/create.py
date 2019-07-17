import json
import logging
import os
import uuid
from datetime import datetime

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def create(event, context):
    data = json.loads(event['body'])
    if 'id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")


    item = {
        #'id': str(uuid.uuid1()),
        'id': data['id'],
        'name': data['name'],
        'email': data['email']
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
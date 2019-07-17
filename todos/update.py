import json
import logging
import os

import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
def update(event, context):
    data = json.loads(event['body'])
    if 'id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return



    # update the todo in the database
    # result = table.update_item(
    #     Key={
    #         'id': event['pathParameters']['id']
    #     },
    #     ExpressionAttributeNames={
    #       '#todo_id': 'id',
    #     },
    #     ExpressionAttributeValues={
    #       ':id': data['id'],
    #       ':name': data['name'],
    #       ':email': data['email'],
    #     },
    #     UpdateExpression='SET #todo_id = :id, '
    #                      'name = :name, '
    #                      'email = :email, ',
    #     ReturnValues='ALL_NEW',
    # )

    # create a response
    response = {
        "statusCode": 200,
        # "body": json.dumps(result['Attributes'])
        "body":json.dumps("Update called for "+ event['pathParameters']['id'])
    }

    return response
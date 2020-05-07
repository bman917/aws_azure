import json
from src import datalex

def hello(event, context):

    body = datalex.calculate(event["queryStringParameters"])

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

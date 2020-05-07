##########
#  AWS   #
##########

import json
from src import datalex
from src import database

def hello(event, context):

    mongodb = database.MongoDB_Collection()

    body = datalex.calculate(
            event["queryStringParameters"],
            mongodb)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

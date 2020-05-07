##########
#  AZURE #
##########

import azure.functions as func
import json
from . import datalex
from . import database

def hello(req):

    mongodb = database.MongoDB_Collection()

    body = datalex.calculate(
            req.params,
            mongodb)

    response = func.HttpResponse(
        status_code=200,
        body=json.dumps(body)
    )

    return response

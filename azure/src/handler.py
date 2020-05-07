import azure.functions as func
from . import datalex

def hello(req):

    body = datalex.calculate(req.params)

    response = func.HttpResponse(
        status_code=200,
        body=body
    )

    return response

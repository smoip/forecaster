import json
from dynamo_wrapper import DynamoDB

def ping(event, context):
    pong = "pong"
    return build_response(200, pong)

def test_read(event, context):
    dynamo_db = DynamoDB()
    resp = dynamo_db.find('12345')
    return build_response(200, resp)

def test_write(event, context):
    dynamo_db = DynamoDB()
    resp = dynamo_db.write('54321', { 'tomorrow': { 'S': 'fucking beautiful' } })
    return build_response(200, resp)

def build_response(code, body):
    return {
        "statusCode": code,
        "body": json.dumps(body)
    }

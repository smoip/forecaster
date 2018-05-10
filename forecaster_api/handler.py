import json

def ping(event, context):
    pong = "pong"
    return build_response(200, pong)

def build_response(code, body):
    return {
        "statusCode": code,
        "body": json.dumps(body)
    }

import os
import json
from dynamo_wrapper import DynamoDB
import requests

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

def test_fetch_forecast(event, context):
    params = json.loads(event['body'])
    try:
        zip_code = params['zip_code']
    except KeyError:
        return build_response(400, "error: please supply a zip_code")

    wunderground_url = f'http://api.wunderground.com/api/{wundergound_api_key()}/forecast/q/{zip_code}.json'
    req = requests.get(wunderground_url)
    return build_response(200, json.loads(req.text))

def get_forecast(zip_code):
    wunderground_url = f'http://api.wunderground.com/api/{wundergound_api_key()}/forecast/q/{zip_code}.json'
    req = requests.get(wunderground_url)
    return req.json


def wundergound_api_key():
    return os.environ['wunderground_api_key']


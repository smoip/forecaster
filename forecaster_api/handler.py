import os
import json
from dynamo_wrapper import DynamoDB
import requests

#  public handlers

def ping(event, context):
    pong = "pong"
    return build_response(200, pong)

def fetch_forecast(event, context):
    params = json.loads(event['body'])
    try:
        zip_code = params['zip_code']
    except KeyError:
        return build_response(400, { 'error' : 'please supply a zip_code' })
    dynamo_db = DynamoDB()
    existing = dynamo_db.find(zip_code)
    try:
        old_ts = existing['timestamp']
        if TimeHandler().stale_timestamp(old_ts):
            forecast = refresh_forecast(zip_code, False)
        else:
            forecast = existing
    except KeyError:
        forecast = refresh_forecast(zip_code, True)

    forecast = json.loads(forecast)

    return build_response(200, forecast)

# internal methods

def refresh_forecast(zip_code, new_entry):
    forecast = fresh_forecast(zip_code)
    if not forecast:
        return { 'error': 'there was a problem fetching data from the wunderground API' }

    # new djank city, ideally these would be separated by key and stored in a Map entry
    # ...oh well
    forecast = json.dumps(forecast)

    dynamo_db = DynamoDB()
    if new_entry:
        resp = dynamo_db.create(zip_code, forecast)
    else:
        resp = dynamo_db.update(zip_code, forecast)
    return resp


def fresh_forecast(zip_code):
    wunderground_url = f'http://api.wunderground.com/api/{wundergound_api_key()}/forecast/q/{zip_code}.json'
    req = requests.get(wunderground_url)
    return json.loads(req.text)

def wundergound_api_key():
    return os.environ['wunderground_api_key']

def build_response(code, body):
    return {
        "statusCode": code,
        "body": json.dumps(body)
    }

# test methods

def test_read(event, context):
    dynamo_db = DynamoDB()
    resp = dynamo_db.find('12346')
    return build_response(200, resp)

def test_write(event, context):
    dynamo_db = DynamoDB()
    resp = dynamo_db.write('54321', json.dumps({ 'tomorrow': { 'S': 'fucking beautiful' } }))
    return build_response(200, resp)

def test_fetch_forecast(event, context):
    params = json.loads(event['body'])
    try:
        zip_code = params['zip_code']
    except KeyError:
        return build_response(400, "error: please supply a zip_code")

    wunderground_url = f'http://api.wunderground.com/api/{wundergound_api_key()}/forecast/q/{zip_code}.json'
    req = requests.get(wunderground_url)
    return build_response(200, json.loads(req.text))

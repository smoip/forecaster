import boto3
from time_handler import TimeHandler

class DynamoDB(object):
    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.table_name = 'forecast-table'

    def find(self, zip_code):
        response = self.client.get_item(
            TableName=self.table_name,
            Key={
                'zip_code': {
                    'S': zip_code,
                }
            },
            AttributesToGet=[
                'forecast',
                'timestamp',
            ],
            ConsistentRead=True
        )
        return response

    def update(self, zip_code, forecast):
        response = self.client.update_item(
            TableName=self.table_name,
            ExpressionAttributeNames={
                '#FC': 'forecast',
                '#TS': 'timestamp',
            },
            ExpressionAttributeValues={
                ':f': {
                    'S': forecast,
                },
                ':t': {
                    'S': TimeHandler().current_timestamp(),
                },
            },
            Key={
                'zip_code': {
                    'S': zip_code,
                }
            },
            ReturnValues='ALL_NEW',
            UpdateExpression='SET #FC = :f, #TS = :t',
        )
        return response

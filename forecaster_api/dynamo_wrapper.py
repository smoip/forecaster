import boto3
from time_handler import TimeHandler

class DynamoDB(object):
    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.table_name = 'forecast-table'
        #  connect to db or create if necessary

    def find(self, zip_code):
        response = self.client.get_item(
            TableName=self.table_name,
            Key={
                'zip_code': {
                    'S': zip_code,
                }

            },
            ConsistentRead=True
        )
        return response

    def update(self, zip_code, forecast):
        dynamodb_response = self.client.update_item(
            TableName=self.table_name,
            Item={
                'zip_code': {
                    'S': zip_code,
                },
                'timestamp': {
                    'S': TimeHandler().current_timestamp(),
                },
                'forecast': {
                    'S': forecast,
                }
            }
        )

    def create(self, zip_code, forecast):
        dynamodb_response = self.client.put_item(
            TableName=self.table_name,
            Item={
                'zip_code': {
                    'S': zip_code,
                },
                'timestamp': {
                    'S': TimeHandler().current_timestamp(),
                },
                'forecast': {
                    'S': forecast,
                }
            }
        )

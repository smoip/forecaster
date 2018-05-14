import boto3
import datetime

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

    def write(self, zip_code, forecast):
        time_stamp = str(datetime.datetime.now())

        dynamodb_response = self.client.put_item(
            TableName=self.table_name,
            Item={
                'zip_code': {
                    'S': zip_code,
                },
                'time_stamp': {
                    'S': time_stamp,
                },
                'forecast': {
                    'M': forecast,
                }
            }
        )


        

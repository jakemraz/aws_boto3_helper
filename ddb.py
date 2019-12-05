import boto3

class Ddb:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
    def put_item(self, item):
        table = self.dynamodb.Table(self.table_name)
        response = table.put_item(
            Item = item
        )

        return response

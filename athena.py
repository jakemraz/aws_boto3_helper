import boto3


class Athena:
    def __init__(self, database):
        self.database = database
        self.client = boto3.client('athena')

    #Function for starting athena query
    def run_query(self, query, s3_output):
        response = self.client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': self.database
                },
            ResultConfiguration={
                'OutputLocation': s3_output,
                }
            )
        print('Execution ID: ' + response['QueryExecutionId'])
        return response

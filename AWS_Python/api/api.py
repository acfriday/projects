import os
import boto3
import flask
from botocore.exceptions import ClientError
from flask import request, jsonify


os.environ['AWS_Profile'] = 'projects'

app = flask.Flask(__name__)
app.config['DEBUG'] = True

dynamodb = boto3.resource('dynamodb')
table_name = 'BBallTable'
table = dynamodb.Table(table_name)

def create_table_if_not_exists():
    try:
        table.load()
        print('Table exists.')
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print('No current table exists, creating new table')

            table = dynamodb.create_table(
            TableName = table_name,
            KeySchema = [
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }   
            ],
            AttributeDefinitions = [
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput = 
            {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName = table_name)
        print('Table created successfully.')
    
    else:
        print('Failure: ', e)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Test API</h1><p>This site is a prototype API for learning Flask and Python.</p>"


@app.route('/api/v1/resources/teams/all', methods=['GET'])
def api_all():
    response = table.scan()
    teams = response['items']
    return jsonify(teams)


app.run()
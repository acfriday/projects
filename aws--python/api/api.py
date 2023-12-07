import os
import boto3
import flask
from botocore.exceptions import ClientError
from flask import request, jsonify


os.environ['AWS_Profile'] = 'projects' # Pass AWS profile credentials at ~/.aws/credentials

app = flask.Flask(__name__) # Create Flask app
app.config['DEBUG'] = True

dynamodb = boto3.resource('dynamodb') # Create DBTable
table_name = 'BBallTable'
table = dynamodb.Table(table_name)

def create_table_if_not_exists(): # Check if table already exist and create one if it doesn't
    try:
        table.load()
        print('Table exists.')
    except ClientError as err: # AWS Docs: "The most common botocore exception you’ll encounter is ClientError. This is a general exception when an error response is provided by an AWS service to your Boto3 client’s request"
        if err.response['Error']['Code'] == 'ResourceNotFoundException':
            print('No current BBall database table exists, creating new table')

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
        print('Failure: ', err)


@app.route('/', methods=['GET']) # Display header and message when home page is accessed
def home():
    return "<h1>Test API</h1><p>This site is a prototype API for learning Flask and Python.</p>"


@app.route('/api/v1/resources/teams/all', methods=['GET']) # Get request route
def api_all():
    response = table.scan()
    teams = response['items']
    return jsonify(teams)


app.run() # Run Flask app
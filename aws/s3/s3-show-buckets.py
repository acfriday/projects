import os
import boto3
from botocore.exceptions import ClientError
os.environ["AWS_Profile"] = "projects"

def ListBucket():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if not response:
             print("No buckets available to this user")
        else:
             print("##Listing available buckets for this account##")
    except ClientError as e:
        print(f"Error: {e}")

    for bucket in response['Buckets']:
        print(f"Bucket: '{bucket['Name']}'")
ListBucket()
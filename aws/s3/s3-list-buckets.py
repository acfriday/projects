import boto3
from botocore.exceptions import ClientError

aws_service = "s3"
aws_region = "us-east-1"
aws_profile = "projects"

boto3 = boto3.session.Session(profile_name=aws_profile)
def ListBucket():
    try:
        s3 = boto3.client(service_name=aws_service ,region_name=aws_region)
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
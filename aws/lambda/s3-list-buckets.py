import boto3
from botocore.exceptions import ClientError

def ListBucket(num):
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        count = 0
        if not response:
            print("No Buckets available to this user")
    except ClientError as e:
        print(f"Error: {e}")
    
    for bucket in response['Buckets']:
        if count < num:
            print(f"#Listing S3 Bucket at index [{count}]")
            bucket_name = bucket['Name']
            bucket_creation = bucket['CreationDate']
            print(f"#Bucket Name: {bucket_name}\n#CreationDate: {bucket_creation}\n")
            count += 1
        else:
            return
ListBucket(0)
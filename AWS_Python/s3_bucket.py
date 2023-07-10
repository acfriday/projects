import boto3
import botocore.exceptions
import os

os.environ['AWS_PROFILE'] = 'projects' # Pass AWS profile credentials at ~/.aws/credentials
s3 = boto3.client('s3') # S3 client
bucket_name = 'devbucket4testing123767884' # Define the bucket name

try: # Create bucket with versioning enabled
    s3.create_bucket(Bucket=bucket_name)
    print(f'Bucket {bucket_name} created succesfully.')
    # Enable versioning
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )
    print(f'Versioning enabled for bucket {bucket_name} successfully.')
    
except botocore.exceptions.ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'BucketAlreadyOwnedByYou':
        print(f'Error: Bucket "{bucket_name}" already exists and is owned by you.')
    elif error_code == 'BucketAlreadyExists':
        print(f'Error: Bucket "{bucket_name}" already exists and is owned by another account.')
    else:
        print(f'Error: {e.response["Error"]["Message"]}')
import boto3
from botocore.exceptions import ClientError

service = "iam"
region = "us-east-1"
profile = "projects"

boto3 = boto3.session.Session(profile_name=profile)
iam = boto3.resource(service_name=service,region_name=region)
try:
    iam_users = iam.users.all()
except ClientError as e:
    print(f"Error loading IAM users: {e.response["Error"]["Message"]}")
for user in iam_users:
    print(f"IAMUser: {user.user_name}")

    
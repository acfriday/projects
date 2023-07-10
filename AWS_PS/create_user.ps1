# Assign variables and use AWS profile at ~/.aws/credential to authenticate
Import-Module AWSPowerShell.NetCore

$Creds = Set-AWSCredential -ProfileName 'projects'
$Group = 'developer'
$Name = 'Dev1'

#Create New IAM User
New-IAMUser -UserName $Name $Creds

# Create New IAM Group
New-IAMGroup -GroupName $Group $Creds


# Register relevant Policies to Group
Register-IAMGroupPolicy -Select ^GroupName $Group -PolicyArn arn:aws:iam::aws:policy/AmazonS3FullAccess -Credential $Creds
Register-IAMGroupPolicy -Select ^GroupName $Group -PolicyArn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess -Credential $Creds

# Add New User to Group to gain permissions
Add-IAMUserToGroup -UserName $Name -GroupName $Group

# Added password by setting password as $PW variable in termnial for this session
New-IAMLoginProfile -Select ^UserName $Name -Password ($PW).ToString() -PasswordResetRequired $false -Credential $Creds


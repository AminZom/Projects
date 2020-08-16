import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        toCopy = {
            'Bucket': record['s3']['bucket']['name'],
            'Key': record['s3']['object']['key']
        }
        bucket = s3.Bucket('msheikht-bucket')
        bucket.copy(toCopy, '1300AssignmentCopy.pdf')

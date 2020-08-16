import boto3
import time

print('Uploading Files...')

startTime = time.time()
s3 = boto3.resource('s3')
path = '../PDFs/'
data = open(path + '1300Assignment1.pdf', 'rb')

bucket = 'msheikht-bucket'

s3.create_bucket(Bucket=bucket)

s3.Bucket(bucket).put_object(Key='1300Assignment1.pdf', Body=data)

endTime = time.time()
print('Time to upload: ', endTime - startTime, ' seconds.')
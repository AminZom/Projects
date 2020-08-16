import boto3
import time

startTime = time.time()
dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')

movieTable = dynamoDB.create_table(
	TableName='msheikht_movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
endTime = time.time()
print("Database successfully created.")
print('Time to create database: ', endTime - startTime, ' seconds.')
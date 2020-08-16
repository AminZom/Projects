import boto3
import json
import decimal
import time

startTime = time.time()
dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')

movieTable = dynamoDB.Table('msheikht_movies')

with open("../moviedata.json") as jsonFile:
    movies = json.load(jsonFile, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie: ", year, title)

        movieTable.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )

endTime = time.time()
print('Successfully populated the table using the JSON file.')
print('Time to populate: ', endTime - startTime, ' seconds.')
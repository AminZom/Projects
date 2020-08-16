import json
import decimal
import os
import time

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

startTime = time.time()

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

connection_str = os.environ['AZURE_TABLE_CONNECTION_STRING']

table_service = TableService(connection_string=connection_str)

with open("../moviedata.json") as jsonFile:
  movies = json.load(jsonFile, parse_float = decimal.Decimal)
for movie in movies:
    year = str(int(movie['year']))
    title = str(movie['title'])
    title = title.replace('\\', '©')
    title = title.replace('?', '®')
    title = title.replace('/', '℗')
    title = title.replace('#', '⨝')
    movieToBeAdded = Entity()
    movieToBeAdded.PartitionKey = year
    movieToBeAdded.RowKey = title
    jsonDump = json.dumps(movie['info'], cls=DecimalEncoder)
    tableJSON = json.loads(jsonDump)
    for i in tableJSON:
        if isinstance(tableJSON[i], list) == True:
            csvString = ''
            for j in tableJSON[i]:
                csvString = csvString + str(j) + ','
            csvString = csvString[:-1]
            movieToBeAdded[i] = csvString
        elif i == 'rank' or i == 'running_time_secs' or i == 'rating':
            movieToBeAdded[i] = float(tableJSON[i])
        else:
            movieToBeAdded[i] = tableJSON[i]
        csvString = ''
    print("Adding movie:", year, title)
    table_service.insert_entity('msheikht_movies', movieToBeAdded)

endTime = time.time()
print("'Successfully populated the table using the JSON file.")
print('Time to populate: ', endTime - startTime, ' seconds.')
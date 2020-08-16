import json
import decimal
import time
import os
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

connection_str = os.environ['AZURE_TABLE_CONNECTION_STRING']

startTime = time.time()
table_service = TableService(connection_string=connection_str)
table_service.create_table('msheikht_movies')

endTime = time.time()
print("Table successfully created.")
print('Time to create table: ', endTime - startTime, ' seconds.')
import json
import decimal
import time
import os
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from prettytable import PrettyTable

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

check = 0
while check == 0:
	primaryExpression = ""
	partitionKeyInput = input('Primary/Partition Key [Individual/Range]=> ')
	if partitionKeyInput == 'Individual':
		partIndivVal = input('Individual Value=> ')
		if partIndivVal.isdigit() == False:
			print('Invalid Input! Please try again.')
			continue
		primaryExpression = "PartitionKey eq '" + partIndivVal + "'"
	elif partitionKeyInput == 'Range':
		print('Which range structure would you like to use?:')
		print('    (1) Less than (year < #)')
		print('    (2) Greater than (year > #)')
		print('    (3) Both (# < year < #)')
		userInput = input('=> ')
		if userInput == '1':
			print('Enter the upper limit (year < #):')
			upperLimit = input('=> ')
			if upperLimit.isdigit() == False:
				print('Invalid Input! Please try again.')
				continue
			primaryExpression = "PartitionKey lt '" + upperLimit + "'"
		elif userInput == '2':
			print('Enter the lower limit (# < year):')
			lowerLimit = input('=> ')
			if lowerLimit.isdigit() == False:
				print('Invalid Input! Please try again.')
				continue
			primaryExpression = "PartitionKey gt '" + lowerLimit + "'"
		elif userInput == '3':
			print('Enter the upper limit (year < #):')
			upperLimit = input('=> ')
			print('Enter the lower limit (# < year):')
			lowerLimit = input('=> ')
			if upperLimit.isdigit() == False or lowerLimit.isdigit() == False:
				print('Invalid Input! Please try again.')
				continue
			primaryExpression = "PartitionKey lt '" + upperLimit + "' and PartitionKey gt '" + lowerLimit + "'"
		else:
			print('Invalid Input! Please try again.')
			continue
	else:
		print('Invalid Input! Please try again.')
		continue
	
	sortKeyInput = input('(Optional) Secondary/Sort Key [Individual/Range]=> ')
	if sortKeyInput == 'Individual':
		sortIndivVal = input('Individual Value=> ')
		primaryExpression = primaryExpression + " and RowKey eq '" + sortIndivVal + "'"
	elif sortKeyInput == 'Range':
		print('Which range structure would you like to use?:')
		print('    (1) Less than (ex. title < L)')
		print('    (2) Greater than (ex. title > A)')
		print('    (3) Both (ex. A < title < L)')
		userInput = input('=> ')
		if userInput == '1':
			print('Enter the upper limit (ex. title < L):')
			upperTitleLimit = input('=> ')
			primaryExpression = primaryExpression + " and RowKey lt '" + upperTitleLimit + "'"
		elif userInput == '2':
			print('Enter the lower limit (ex. A < title):')
			lowerTitleLimit = input('=> ')
			primaryExpression = primaryExpression + " and RowKey gt '" + lowerTitleLimit + "'"
		elif userInput == '3':
			print('Enter the upper limit (ex. title < L):')
			upperTitleLimit = input('=> ')
			print('Enter the lower limit (ex. A < title):')
			lowerTitleLimit = input('=> ')
			primaryExpression = primaryExpression + " and RowKey lt '" + upperTitleLimit + "' and RowKey gt '" + lowerTitleLimit + "'"
		else:
			print('Invalid Input! Please try again.')
			continue
	elif sortKeyInput == '':
		print('Skipping sort key.')
	else:
		print('Invalid Input! Please try again.')
		continue

	filterInput = input('(Optional) Filters (ex. rating gt 3)=> ')
	if filterInput != '':
		filterInputList = filterInput.split(" ")
		if len(filterInputList) != 3:
			print('Invalid Input! Input example: "rating gt 3".')
			continue
		primaryExpression = primaryExpression + " and " + filterInput
	else:
		print('Skipping filters.')

	outputTable = PrettyTable()
	outputTable.field_names = ["Year", "Title", "Rating", "Rank"]

	sortInput = input('(Optional) Sort [Primary/Secondary/Other]=> ')
	if sortInput != '':
		if sortInput == 'Primary':
			outputTable.sortby = "Year"
			outputTable.reversesort = True
		elif sortInput == 'Secondary':
			outputTable.sortby = "Title"
			outputTable.reversesort = False
		elif sortInput == 'Other':
			print('Which attribute would you like to sort by?:')
			print('    (1) Rating')
			print('    (2) Rank')
			userInput = input('=> ')
			if userInput == '1':
				outputTable.sortby = "Rating"
				outputTable.reversesort = True
			elif userInput == '2':
				outputTable.sortby = "Rank"
				outputTable.reversesort = False
			else:
				print('Skipping sorting due to invalid selection.')
		else:
			print('Invalid Input! Input example: "info.rating gt 3".')
			continue
	else:
		print('Skipping sorting.')

	displayFields = []
	fileFields = []
	print('(Optional) Choose any or all of the following fields/attributes by providing a comma-separated list:')
	print('Example: "Primary, Secondary, rank" :')
	print('    - Primary')
	print('    - Secondary')
	print('    - rating')
	print('    - rank')
	fieldInput = input('=> ')
	if fieldInput != '':
		fieldInputList = fieldInput.split(", ")
		if len(set(fieldInputList)) != len(fieldInputList):
			print('Invalid input! Input example: "Primary, Secondary, rating".')
			continue
		checkError = 0
		for field in fieldInputList:
			if field == 'Primary':
				displayFields.append("Year")
				fileFields.append('PartitionKey')
			elif field == 'Secondary':
				displayFields.append("Title")
				fileFields.append('RowKey')
			elif field == 'rating':
				displayFields.append("Rating")
				fileFields.append('rating')
			elif field == 'rank':
				displayFields.append("Rank")
				fileFields.append('rank')
			else:
				checkError = 1
				continue
		if checkError == 1:
			print('Skipping fields/attributes due to invalid input.')
			fileFields = ['PartitionKey', 'RowKey', 'rating', 'rank']
	else:
		print('Skipping fields/attributes.')
		fileFields = ['PartitionKey', 'RowKey', 'rating', 'rank']

	startTime = time.time()
	response = None
	ratingCount = 0
	
	movies = table_service.query_entities('msheikht_movies', filter = primaryExpression)
	for movie in movies:
		try:
			movie.RowKey = movie.RowKey.replace('©', '\\')
			movie.RowKey = movie.RowKey.replace('®', '?')
			movie.RowKey = movie.RowKey.replace('℗', '/')
			movie.RowKey = movie.RowKey.replace('⨝', '#')
			outputTable.add_row([movie.PartitionKey, movie.RowKey, movie.rating, movie.rank])
		except AttributeError as ex:
			ratingCount = ratingCount + 1
			outputTable.add_row([movie.PartitionKey, movie.RowKey, 0, movie.rank])

	print(outputTable.get_string(fields=displayFields))
	if ratingCount != 0:
		print(str(ratingCount) + ' movies did not have a rating, so they were set to 0.')
	endTime = time.time()
	print('Time to perform query: ', endTime - startTime, ' seconds.')
	userInput = input('Would you like to save these results to a file? (y/n)=> ')
	if userInput == 'y':
		userInput = input('Please enter a name for the CSV file=> ')
		try:
			csvFile = open(userInput, "w")
			movies = table_service.query_entities('msheikht_movies', filter = primaryExpression)
			for movie in movies:
				movie.RowKey = movie.RowKey.replace('©', '\\')
				movie.RowKey = movie.RowKey.replace('®', '?')
				movie.RowKey = movie.RowKey.replace('℗', '/')
				movie.RowKey = movie.RowKey.replace('⨝', '#')
				toFileStr = ''
				for fileField in fileFields:
					if fileField == 'rating':
						try:
							checkStr = str(movie.rating)
							toFileStr = toFileStr + checkStr + ','
						except AttributeError as el:
							toFileStr = toFileStr + '0,'
					elif fileField == 'rank':
						toFileStr = toFileStr + str(movie.rank) + ','
					else:
						if "," in str(movie[fileField]):
							toFileStr = toFileStr + '"' + str(movie[fileField]) + '"' + ','
						else:
							toFileStr = toFileStr + str(movie[fileField]) + ','
				toFileStr = toFileStr[:-1] + '\n'
				csvFile.write(toFileStr)
			csvFile.close()
		except Exception as ex:
			print(str(ex))
			print('Invalid file name! Please try again.')
			continue
	check = 1

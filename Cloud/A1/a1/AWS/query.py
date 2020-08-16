import boto3
import json
import decimal
import time
from boto3.dynamodb.conditions import Key, Attr
from prettytable import PrettyTable

dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
movieTable = dynamoDB.Table('msheikht_movies')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

check = 0
while check == 0:
	primaryExpression = None
	secondaryExpression = None
	sortKeyCheck = 0
	filterCheck = 0
	partitionKeyInput = input('Primary/Partition Key [Individual/Range]=> ')
	if partitionKeyInput == 'Individual':
		partIndivVal = input('Individual Value=> ')
		if partIndivVal.isdigit() == False:
			print('Invalid Input! Please try again.')
			continue
		primaryExpression = Key('year').eq(int(partIndivVal))
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
			primaryExpression = Key('year').lt(int(upperLimit))
		elif userInput == '2':
			print('Enter the lower limit (# < year):')
			lowerLimit = input('=> ')
			if lowerLimit.isdigit() == False:
				print('Invalid Input! Please try again.')
				continue
			primaryExpression = Key('year').gt(int(lowerLimit))
		elif userInput == '3':
			print('Enter the upper limit (year < #):')
			upperLimit = input('=> ')
			print('Enter the lower limit (# < year):')
			lowerLimit = input('=> ')
			if upperLimit.isdigit() == False or lowerLimit.isdigit() == False or int(upperLimit) < int(lowerLimit):
				print('Invalid Input! Please try again.')
				continue
			primaryExpression = Key('year').between(int(lowerLimit), int(upperLimit))
		else:
			print('Invalid Input! Please try again.')
			continue
	else:
		print('Invalid Input! Please try again.')
		continue
	
	sortKeyInput = input('(Optional) Secondary/Sort Key [Individual/Range]=> ')
	if sortKeyInput == 'Individual':
		sortKeyCheck = 1
		sortIndivVal = input('Individual Value=> ')
		secondaryExpression = Key('title').eq(sortIndivVal)
	elif sortKeyInput == 'Range':
		sortKeyCheck = 1
		print('Which range structure would you like to use?:')
		print('    (1) Less than (ex. title < L)')
		print('    (2) Greater than (ex. title > A)')
		print('    (3) Both (ex. A < title < L)')
		userInput = input('=> ')
		if userInput == '1':
			print('Enter the upper limit (ex. title < L):')
			upperTitleLimit = input('=> ')
			secondaryExpression = Key('title').lt(upperTitleLimit)
		elif userInput == '2':
			print('Enter the lower limit (ex. A < title):')
			lowerTitleLimit = input('=> ')
			secondaryExpression = Key('title').gt(lowerTitleLimit)
		elif userInput == '3':
			print('Enter the upper limit (ex. title < L):')
			upperTitleLimit = input('=> ')
			print('Enter the lower limit (ex. A < title):')
			lowerTitleLimit = input('=> ')
			secondaryExpression = Key('title').between(lowerTitleLimit, upperTitleLimit)
		else:
			print('Invalid Input! Please try again.')
			continue
	elif sortKeyInput == '':
		print('Skipping sort key.')
	else:
		print('Invalid Input! Please try again.')
		continue

	filterInput = input('(Optional) Filters (ex. info.rating gt 3)=> ')
	if filterInput != '':
		filterInputList = filterInput.split(" ")
		if len(filterInputList) != 3:
			print('Invalid Input! Input example: "info.rating gt 3".')
			continue
		if filterInputList[1] == 'eq':
			if filterInputList[0] == 'info.rating' or filterInputList[0] == 'info.rank' or filterInputList[0] == 'info.running_time_secs':
				try:
					attributeExpression = Attr(filterInputList[0]).eq(int(filterInputList[2]))
				except ValueError as ex:
					print('Invalid Input! Input example: "info.rating gt 3".')
					continue
			else:
				attributeExpression = Attr(filterInputList[0]).eq(filterInputList[2])
			filterCheck = 1
		elif filterInputList[1] == 'gt':
			if filterInputList[0] == 'info.rating' or filterInputList[0] == 'info.rank' or filterInputList[0] == 'info.running_time_secs':
				try:
					attributeExpression = Attr(filterInputList[0]).eq(int(filterInputList[2]))
				except ValueError as ex:
					print('Invalid Input! Input example: "info.rating gt 3".')
					continue
			else:
				attributeExpression = Attr(filterInputList[0]).gt(filterInputList[2])
			filterCheck = 1
		elif filterInputList[1] == 'lt':
			if filterInputList[0] == 'info.rating' or filterInputList[0] == 'info.rank' or filterInputList[0] == 'info.running_time_secs':
				try:
					attributeExpression = Attr(filterInputList[0]).lt(int(filterInputList[2]))
				except ValueError as ex:
					print('Invalid Input! Input example: "info.rating gt 3".')
					continue
			else:
				attributeExpression = Attr(filterInputList[0]).lt(filterInputList[2])
			filterCheck = 1
		else:
			print('Invalid Input! Input example: "info.rating gt 3".')
			continue
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
	print('Example: "Primary, Secondary, info.rank" :')
	print('    - Primary')
	print('    - Secondary')
	print('    - info.rating')
	print('    - info.rank')
	fieldInput = input('=> ')
	if fieldInput != '':
		fieldInputList = fieldInput.split(", ")
		if len(set(fieldInputList)) != len(fieldInputList):
			print('Invalid input! Input example: "Primary, Secondary, info.rating".')
			continue
		checkError = 0
		for field in fieldInputList:
			if field == 'Primary':
				displayFields.append("Year")
				fileFields.append('year')
			elif field == 'Secondary':
				displayFields.append("Title")
				fileFields.append('title')
			elif field == 'info.rating':
				displayFields.append("Rating")
				fileFields.append('info.rating')
			elif field == 'info.rank':
				displayFields.append("Rank")
				fileFields.append('info.rank')
			else:
				checkError = 1
				break
		if checkError == 1:
			print('Skipping fields/attributes due to invalid input.')
			fileFields = ['year', 'title', 'info.rating', 'info.rank']
	else:
		print('Skipping fields/attributes.')
		fileFields = ['year', 'title', 'info.rating', 'info.rank']

	startTime = time.time()
	response = None
	count = 0
	fileExpression = None
	if sortKeyCheck == 0 and filterCheck == 0:
		response = movieTable.scan(
			FilterExpression=primaryExpression
		)
		fileExpression = primaryExpression
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
		while 'LastEvaluatedKey' in response:
			response = movieTable.scan(
				FilterExpression=primaryExpression,
				ExclusiveStartKey=response['LastEvaluatedKey']
			)
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
	elif sortKeyCheck == 1 and filterCheck == 0:
		response = movieTable.scan(
			FilterExpression=primaryExpression & secondaryExpression
		)
		fileExpression = primaryExpression & secondaryExpression
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
		while 'LastEvaluatedKey' in response:
			response = movieTable.scan(
				FilterExpression=primaryExpression & secondaryExpression,
				ExclusiveStartKey=response['LastEvaluatedKey']
			)
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
	elif sortKeyCheck == 0 and filterCheck == 1:
		response = movieTable.scan(
			FilterExpression=primaryExpression & attributeExpression
		)
		fileExpression = primaryExpression & attributeExpression
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
		while 'LastEvaluatedKey' in response:
			response = movieTable.scan(
				FilterExpression=primaryExpression & attributeExpression,
				ExclusiveStartKey=response['LastEvaluatedKey']
			)
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
	else:
		response = movieTable.scan(
			FilterExpression=primaryExpression & secondaryExpression & attributeExpression
		)
		fileExpression = primaryExpression & secondaryExpression & attributeExpression
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
		while 'LastEvaluatedKey' in response:
			response = movieTable.scan(
				FilterExpression=primaryExpression & secondaryExpression & attributeExpression,
				ExclusiveStartKey=response['LastEvaluatedKey']
			)
		for i in response['Items']:
			jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
			tableJSON = json.loads(jsonDump)
			try:
				outputTable.add_row([i['year'], i['title'], tableJSON['rating'], tableJSON['rank']])
			except KeyError as ex:
				count = count + 1
				outputTable.add_row([i['year'], i['title'], 0, tableJSON['rank']])
	print(outputTable.get_string(fields=displayFields))
	if count != 0:
		print(str(count) + ' movies did not have a rating, so they were set to 0.')
	endTime = time.time()
	print('Time to perform query: ', endTime - startTime, ' seconds.')
	userInput = input('Would you like to save these results to a file? (y/n)=> ')
	if userInput == 'y':
		userInput = input('Please enter a name for the CSV file=> ')
		try:
			csvFile = open(userInput, "w")
			response = movieTable.scan(
				FilterExpression=fileExpression
			)
			for i in response['Items']:
				jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
				tableJSON = json.loads(jsonDump)
				toFileStr = ''
				for fileField in fileFields:
					if fileField == 'info.rating':
						try:
							checkStr = str(tableJSON['rating'])
							toFileStr = toFileStr + checkStr + ','
						except KeyError as el:
							toFileStr = toFileStr + '0,'
					elif fileField == 'info.rank':
						toFileStr = toFileStr + str(tableJSON['rank']) + ','
					else:
						toFileStr = toFileStr + str(i[fileField]) + ','
				toFileStr = toFileStr[:-1] + '\n'
				csvFile.write(toFileStr)
			while 'LastEvaluatedKey' in response:
				response = movieTable.scan(
					FilterExpression=fileExpression,
					ExclusiveStartKey=response['LastEvaluatedKey']
				)
			for i in response['Items']:
				jsonDump = json.dumps(i['info'], cls=DecimalEncoder)
				tableJSON = json.loads(jsonDump)
				toFileStr = ''
				for fileField in fileFields:
					if fileField == 'info.rating':
						try:
							checkStr = str(tableJSON['rating'])
							toFileStr = toFileStr + checkStr + ','
						except KeyError as el:
							toFileStr = toFileStr + '0,'
					elif fileField == 'info.rank':
						toFileStr = toFileStr + str(tableJSON['rank']) + ','
					else:
						toFileStr = toFileStr + str(i[fileField]) + ','
				toFileStr = toFileStr[:-1] + '\n'
				csvFile.write(toFileStr)
			csvFile.close()
		except Exception as ex:
			print(type(ex))
			print(str(ex))
			print('Invalid file name! Please try again.')
			continue
	check = 1

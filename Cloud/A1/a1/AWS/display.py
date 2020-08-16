import boto3
import time

s3 = boto3.resource('s3')

userInput = ''
while userInput != 'quit':
	print('What would you like to do?:')
	print('   (1) Display all objects')
	print('   (2) Display objects in a specific container')
	print('   (3) Display a specific object in any container')
	print('   (4) Download a specific object')
	print('   (quit) Quit the program')
	userInput = input('=> ')
	if userInput == '1':
		startTime = time.time()
		for bucket in s3.buckets.all():
			for bucket_object in bucket.objects.all():
				print(bucket_object.key)
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
	elif userInput == '2':
		print('Enter the name of the container:')
		bucketName = input('=> ')
		startTime = time.time()
		bucket = s3.Bucket(bucketName)
		if (bucket in s3.buckets.all()) == False:
			print('Bucket does not exist! Please try again.')
			continue
		for bucket_object in bucket.objects.all():
				print(bucket_object.key)
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
	elif userInput == '3':
		print('Enter the name of the object:')
		objectName = input('=> ')
		startTime = time.time()
		check = 0
		for bucket in s3.buckets.all():
			for bucket_object in bucket.objects.all():
				if bucket_object.key == objectName:
					print(bucket_object.key + ' -> ' + bucket.name)
					check = 1
		if check == 0:
			print('No objects found with the name "' + objectName + '"')
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
	elif userInput == '4':
		print('Enter the name of the object:')
		objectName = input('=> ')
		startTime = time.time()
		check = 0
		for bucket in s3.buckets.all():
			for bucket_object in bucket.objects.all():
				if bucket_object.key == objectName:
					s3.meta.client.download_file(bucket.name, objectName, '../PDFs/' + objectName)
					check = 1
					print('Successfully downloaded file "' + objectName + '" from bucket "' + bucket.name + '"')
		if check == 0:
			print('No objects found with the name "' + objectName + '"')
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

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
		containerList = blob_service_client.list_containers()
		for container in containerList:
			containerClient = blob_service_client.get_container_client(container)
			blobList = containerClient.list_blobs()
			for blob in blobList:
				print(blob.name)
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
	elif userInput == '2':
		print('Enter the name of the container:')
		containerName = input('=> ')
		startTime = time.time()
		try:
			containerClient = blob_service_client.get_container_client(containerName)
			blobList = containerClient.list_blobs()
			for blob in blobList:
				print(blob.name)
		except Exception as ex:
			print('Container does not exist! Please try again.')
			continue
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
	elif userInput == '3':
		print('Enter the name of the object:')
		objectName = input('=> ')
		startTime = time.time()
		check = 0
		containerList = blob_service_client.list_containers()
		for container in containerList:
			containerClient = blob_service_client.get_container_client(container)
			blobList = containerClient.list_blobs()
			for blob in blobList:
				if blob.name == objectName:
					print(blob.name + ' -> ' + container.name)
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
		containerList = blob_service_client.list_containers()
		for container in containerList:
			containerClient = blob_service_client.get_container_client(container)
			blobList = containerClient.list_blobs()
			for blob in blobList:
				if blob.name == objectName:
					check = 1
					blobClient = blob_service_client.get_blob_client(container=container.name, blob=blob.name)
					with open('../PDFs/' + blob.name, "wb") as download_file:
						download_file.write(blobClient.download_blob().readall())
					print('Successfully downloaded file "' + blob.name + '" from container "' + container.name + '"')
		if check == 0:
			print('No objects found with the name "' + objectName + '"')
		endTime = time.time()
		print('Time to display: ', endTime - startTime, ' seconds.')
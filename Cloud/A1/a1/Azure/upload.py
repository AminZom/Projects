import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time

print('Uploading Files...')

startTime = time.time()
path = '../PDFs/'
data1 = open(path + '1300Assignment1.pdf', 'rb')
data2 = open(path + '1300Assignment2.pdf', 'rb')
data3 = open(path + '1300Assignment3.pdf', 'rb')
data4 = open(path + '1300Assignment4.pdf', 'rb')
data5 = open(path + '3110Lecture1.pdf', 'rb')
data6 = open(path + '3110Lecture2.pdf', 'rb')
data7 = open(path + '3110Lecture3.pdf', 'rb')
data8 = open(path + '3110Assignment1.pdf', 'rb')
data9 = open(path + '4010Lecture1.pdf', 'rb')
data10 = open(path + '4010Lecture1.pdf', 'rb')
data11 = open(path + '4010Assignment1.pdf', 'rb')

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container1Name = 'msheikht-cis1300'
container2Name = 'msheikht-cis3110'
container3Name = 'msheikht-cis4010'

containerClient1 = blob_service_client.create_container(container1Name)
containerClient2 = blob_service_client.create_container(container2Name)
containerClient3 = blob_service_client.create_container(container3Name)

blobClient1 = blob_service_client.get_blob_client(container=container1Name, blob='1300Assignment1.pdf')
blobClient2 = blob_service_client.get_blob_client(container=container1Name, blob='1300Assignment2.pdf')
blobClient3 = blob_service_client.get_blob_client(container=container1Name, blob='1300Assignment3.pdf')
blobClient4 = blob_service_client.get_blob_client(container=container1Name, blob='1300Assignment4.pdf')
blobClient5 = blob_service_client.get_blob_client(container=container2Name, blob='3110Lecture1.pdf')
blobClient6 = blob_service_client.get_blob_client(container=container2Name, blob='3110Lecture2.pdf')
blobClient7 = blob_service_client.get_blob_client(container=container2Name, blob='3110Lecture3.pdf')
blobClient8 = blob_service_client.get_blob_client(container=container2Name, blob='3110Assignment1.pdf')
blobClient9 = blob_service_client.get_blob_client(container=container3Name, blob='4010Lecture1.pdf')
blobClient10 = blob_service_client.get_blob_client(container=container3Name, blob='4010Lecture2.pdf')
blobClient11 = blob_service_client.get_blob_client(container=container3Name, blob='4010Assignment1.pdf')

blobClient1.upload_blob(data1)
blobClient2.upload_blob(data2)
blobClient3.upload_blob(data3)
blobClient4.upload_blob(data4)
blobClient5.upload_blob(data5)
blobClient6.upload_blob(data6)
blobClient7.upload_blob(data7)
blobClient8.upload_blob(data8)
blobClient9.upload_blob(data9)
blobClient10.upload_blob(data10)
blobClient11.upload_blob(data11)
endTime = time.time()
print('Time to upload: ', endTime - startTime, ' seconds.')
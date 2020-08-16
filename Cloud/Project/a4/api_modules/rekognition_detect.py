import boto3
import os
import io

def call_rekognition():

    client = boto3.client('rekognition', 'us-east-1')
    file = open('aws_response.txt', "w")

    directory = './resources/'

    for filename in os.listdir(directory):
        with io.open(os.path.join('resources', filename), 'rb') as image_file:
            content = image_file.read()
            response = client.detect_labels(Image={"Bytes":content})
            file.write('Detected labels for ' + filename + '\n') 
            for label in response['Labels']:
                file.write("    " + label['Name'] + " (" + str("%.2f" % label['Confidence']) + "% Confidence)" + '\n')
                if(label['Parents']):
                    file.write("       Parents:\n")
                for parent in label['Parents']:
                    file.write("           " + parent['Name'] + '\n')
    file.close()
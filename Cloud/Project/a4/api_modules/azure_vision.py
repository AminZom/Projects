import os
import sys
import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import time

def az_vision():
    # Add your Computer Vision subscription key and endpoint to your environment variables.
    if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
    else:
        print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
        sys.exit()

    if 'COMPUTER_VISION_ENDPOINT' in os.environ:
        endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

    #analyze_url = endpoint + "/v2.1/analyze"
    tag_url = endpoint + "/v2.1/tag"


    directory = './resources/'

    for filename in os.listdir(directory):

        # Set image_path to the local path of an image that you want to analyze.

        
        # Read the image into a byte array
        print(filename)
        image_data = open(os.path.join('resources', filename), 'rb').read()
        headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Categories,Description,Color'}
        #response = requests.post(
        #    analyze_url, headers=headers, params=params, data=image_data)
        #response.raise_for_status()

        response2 = requests.post(
            tag_url, headers=headers, params=params, data=image_data)
        response2.raise_for_status()

        # The 'analysis' object contains various fields that describe the image. The most
        # relevant caption for the image is obtained from the 'description' property.
        #analysis = response.json()
        analysis2 = response2.json()
        for label in analysis2['tags']:
            print('\t' + label['name'] + ' (' + ("%.2f" % (label['confidence'] * 100)) +'% confidence)')
        print("")
        #print(analysis2)
        #image_caption = analysis["description"]["captions"][0]["text"].capitalize()

        # Display the image and overlay it with the caption.
        #image = Image.open(BytesIO(image_data))
        #plt.imshow(image)
        #plt.axis("off")
        #_ = plt.title(image_caption, size="x-large", y=-0.1)
        #plt.show()
        time.sleep(15)

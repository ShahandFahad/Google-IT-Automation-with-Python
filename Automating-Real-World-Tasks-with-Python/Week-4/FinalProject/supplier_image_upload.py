#!/usr/bin/env python3
import requests
import os
url = "http://localhost/upload/"
images_dir = "supplier-data/images/"

for image in os.listdir(images_dir):
    if image.endswith('.jpeg'):
        with open((images_dir + image), 'rb') as opened:
            # print(opened)
            # print(image)
            print(image, opened)
            print("Post Request")
            response = requests.post(url, files={'file' : opened})
            response.raise_for_status()
            print(response.status_code)
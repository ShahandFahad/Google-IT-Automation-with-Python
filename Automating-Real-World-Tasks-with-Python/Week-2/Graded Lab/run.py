#! /usr/bin/env python3
import os
import requests
import json

text_files_path = '/data/feedback/'
feedback_dict = {}
# Store keys for the dictionary
keys = ['title', 'name, ', 'date', 'feedback']

# Access fils in the directory
for file in os.listdir(text_files_path):

# only operate on .txt files
    if file.endswith('.txt'):
        print(file)
        # open each file and read line by line
        with open((text_files_path + file), mode='r') as t_file:
            file_data = t_file.readlines()
        # Sotre data in dictionary
        i = 0
        for data in file_data:
            feedback_dict[keys[i]] = data
            i += 1
        print()
        print(feedback_dict)
        print()
        # Make a post request by sending data in json format in specfied format
        print("Post Request")
        url = "http://34.69.163.70/feedback/"
        response = requests.post(url, json = feedback_dict)
        response.raise_for_status()
        print(response.status_code)
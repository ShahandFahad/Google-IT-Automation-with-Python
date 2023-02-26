#!/usr/bin/env python3
import os
import requests

fruit_description_path = "supplier-data/descriptions/"

keys = ["name", "weight", "description", "image_name"]
fruit_dic = {}
for file in os.listdir(fruit_description_path):
    with open((fruit_description_path + file), 'r') as fruit:
        file_data = fruit.readlines()
        
    # Sotre data in dictionary
    # remove Ibs form weight and convert it to string    
    # print(type(int(file_data[1].strip("Ibs\n"))))
    file_data[1] = int(file_data[1].strip(" lbs\n"))
    i = 0
    for data in file_data:
        fruit_dic[keys[i]] = data
        i += 1
    # file and image names are same just replace .txt with .jepg for specific file
    fruit_dic['image_name'] = file.replace('.txt' , '.jpeg')
    # print(file.replace('.txt' , '.jpeg'))
    print()
    print(fruit_dic)
    print()        
    
    # Make a post request by sending data in json format in specfied format
    print("Post Request")
    url = "http://[linux-instance-external-IP]/fruits/"
    response = requests.post(url, json = fruit_dic)
    response.raise_for_status()
    print(response.status_code)
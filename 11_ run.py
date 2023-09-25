#!/usr/bin/env python3

import os
import requests
import json

descriptions_path = "supplier-data/descriptions"

#------------------------------------------------------------------------------ Generate list of txt files with Fruit Descriptions.
file_list = os.listdir(descriptions_path)
print(f"List of descriptions files: {file_list}.")

#--------------------------------------------------------------------------------------- Generate Dictionary of Fruit Descriptions.
def descriptions_dict(file_list):
    descriptions_dictionary = {}
    for description_file in file_list:
        file_path = os.path.join(descriptions_path, description_file)
        with open(file_path, 'r') as file:
            name = file.readline().strip()    #-------------------------------------------------------- Name of the fruit received.
            weight = float(file.readline().replace('lbs', '').strip())    #------------------- Weight of the fruit received as integer.
            description = file.read().strip()     # Description of the fruit
            image_name = description_file.split(".")[0] + ".jpeg" # Name of the fruit's image
            descriptions_dictionary[description_file] = {'name': name, 'weight': weight, 'description': description, 'image_name': image_name}
    print(f"Dictionary of Fruit descriptions: {descriptions_dictionary}.")
    return descriptions_dictionary   

#---------------------------------------------------------------------------------------------- Post Fruit descriptions on webpage.
def post_descriptions(descriptions):
    for description_file, description in descriptions.items():    #------------ (dictionary with dictionaries, internal dictionary)
        description_json = json.dumps(description)    #------------------------------- Convert the review dictionary to JSON format
        response = requests.post("http://35.196.222.64/fruits/api", data=description_json, headers={"Content-Type": "application/json"})

        if response.status_code == 201:
            print(f"Description {description_file} posted successfully.")
        else:
            print(f"Failed to post Description {description_file}. Status code: {response.status_code}")

#----------------------------------------------------------------------------------------------------------- Call to Main function.
if __name__ == "__main__":

    descriptions = descriptions_dict(file_list)
    post_descriptions(descriptions)

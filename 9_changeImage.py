#!/usr/bin/env python3

from PIL import Image
import os

directory = "supplier-data/images"
output_directory = "supplier-data/images"

#The for loop to correct the badly formatted images.
for filename in os.listdir(directory):
    if filename.endswith(".tiff"):
        im = Image.open(os.path.join(directory, filename))    #os.path.join() is used to construct the full path to the file.
        im = im.resize((600,400))
        im = im.convert("RGB")    #Ensure image is in RGB mode. This is necessary if the original image was in a different color format.
        base_filename = os.path.splitext(filename)[0]    #This removes the .tiff extension from the filename
        im.save(os.path.join(output_directory, base_filename+".jpeg"))  

        
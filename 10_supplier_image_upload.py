#!/usr/bin/env python3

import requests
import os

directory = "supplier-data/images"

url = "http://34.136.40.123/upload/" # TODO: Cambiar esta línea más tarde

for filename in os.listdir(os.path.expanduser(directory)):
    if filename.endswith(".jpeg"):
        with open(os.path.join(os.path.expanduser(directory), filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})


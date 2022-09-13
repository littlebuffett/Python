from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import base64
import json
import time
import os

user = "user"
password = "pass"

url = "https://example.com/wp-json/wp/v2"
data_string = user + ':' + password

token = base64.b64encode(data_string.encode())

headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

image = {
    "file": open("toto.png", "rb"),
    "caption": "caption",
    "description": "description",
}

r = requests.post(url + "/media", headers=headers, files=image)
print(r.text)
print(r)
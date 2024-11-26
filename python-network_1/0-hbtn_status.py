#!/usr/bin/python3

import urllib.request

url = 'http://0.0.0.0:5050/status'  

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))

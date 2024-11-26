#!/usr/bin/python3

import urllib.request
import os

# Use a default URL, but allow override via environment variable
url = os.getenv('TEST_URL', 'https://alu-intranet.hbtn.io/status')

# Send the request and handle the response
with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))

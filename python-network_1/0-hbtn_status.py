#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
using urllib and displays information about the response body:
- The type of the content
- The content in raw bytes
- The content decoded in UTF-8
"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

# Send the request and handle the response
with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))

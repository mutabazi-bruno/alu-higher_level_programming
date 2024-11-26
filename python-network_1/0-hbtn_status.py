#!/usr/bin/python3

import urllib.request

# Update the URL as required by the test
url = 'http://0.0.0.0:5050/status'

# Define the headers
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
    )
}

# Make the request
req = urllib.request.Request(url, headers=headers)

# Use the `with` statement to handle the request and response
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))
i


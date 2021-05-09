import requests
import sys
import json




resp = requests.get("https://api.github.com/users/khanhnt99/repos")
data = resp.json()

print(data)






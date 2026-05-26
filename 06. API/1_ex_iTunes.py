""" 
Write a Python script that:
  - uses the iTunes Search API
  - takes an artist name as a command-line argument
  - fetches up to 50 songs for that artist
  - prints the names of the songs returned by the API.  """

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

data = response.json()

for result in data["results"]:
    print(result["trackName"])

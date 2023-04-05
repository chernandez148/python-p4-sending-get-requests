import requests
import json

url = "https://alpha-vantage.p.rapidapi.com/query"

response = requests.get(url)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))

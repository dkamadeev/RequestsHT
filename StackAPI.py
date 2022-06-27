import requests
from pprint import pprint

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1656115200&todate=1656288000&order=desc&sort=activity&site=stackoverflow'
response = requests.get(url)
for i in response.json()['items']:
    for b in i['tags']:
        if b == 'python':
            print(i['title'])


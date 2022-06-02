#python script to download each item to put into a database to randomize
import requests
from requests import status_codes

arr = []

baseURL = "https://www.dnd5eapi.co"

response = requests.get(baseURL + "/api/magic-items")
statusCode = response.status_code
print(statusCode)
if statusCode != 200:
    print("Error connecting to API, closing")
    exit(0)

monJSON = response.json()

for i in range(0, monJSON['count']):
    arr.append(monJSON['results'][i]['name'])


file = open("../D&DRandomizer/Magic-itemsDB.txt", 'w')
for item in arr:
    file.write(item)
    file.write('\n')
    file.write('\n')

file.close()
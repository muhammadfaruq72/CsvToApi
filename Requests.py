#!/usr/bin/env python3

import requests
import json

some_info = {
	"directory": "hey"
}


head = 'http://127.0.0.1:8000'
Select_csv = requests.post(f'{head}/directory', data=json.dumps(some_info))
Select_csv = json.loads(Select_csv.text)
print(Select_csv)


fileName = Select_csv[0][:Select_csv[0].index(".")]
columnName = "Email"


def getAllData(fileName):
	get = requests.get(f'{head}/{fileName}', data=json.dumps(some_info))
	get = get.json()
	#get = json.loads(get)
	#print(get)

getAllData(fileName)


def query(fileName, columnName):
	get = requests.get(f'{head}/{fileName}/{columnName}', data=json.dumps(some_info))
	get = get.json()
	print(get)
	
query(fileName, columnName)

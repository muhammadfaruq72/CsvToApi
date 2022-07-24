#!/usr/bin/env python3

import pandas as pd
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import json
import csv


load_dotenv()

app = FastAPI()

# <-- importing CSV -->
try:
	path = os.getenv("DIRECTORY")
	listfiles = os.getenv("DIRECTORY")
	listfiles = [file for file in os.listdir(listfiles) if file.endswith((".csv")) ]
	
	get_csv = []
	for x in listfiles:
		get_csv.append(x)
	
	
	@app.post("/Select_csv")
	def test_function(dict: dict[str, str]):
		print(dict)
		# do something
		return get_csv
except:
	path = os.getenv("URL")
	
@app.get("/{fileName}")
async def read_item(fileName):
	# <-- Reading Full CSV -->
	print(path)
	path_to_csv = f'{path}/{fileName}.csv'
	df = pd.read_csv(path_to_csv)
	df= df.to_json(orient='records')
	df = json.loads(df)
	return df

@app.get("/{fileName}/{Column}")
async def query(fileName, Column, value):
	# <-- Reading Specific CSV -->
	print(path)
	path_to_csv_1 = f'{path}/{fileName}.csv'
	df = pd.read_csv(path_to_csv_1)
	df= df.to_json(orient='records')
	df = json.loads(df)
	
	if value.isdigit():
		value = int(value)
	else:
		""
		
	df = list(filter(lambda x:x[Column]==value,df))
	print(df)
	#df = json.dumps(df)
	
	return df

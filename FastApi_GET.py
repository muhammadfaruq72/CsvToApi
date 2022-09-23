#!/usr/bin/env python3

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel
import os, json, webbrowser
from threading import Timer

print(os.getcwd())

load_dotenv()

app = FastAPI()

def readenv():
	r = open(".env", "r+")
	path = r.read()
	return path


templates = Jinja2Templates(directory="templates")

class iRequest(BaseModel):
	directory: str

	
# <-- importing CSV -->
try:
	
	
	class iRequest(BaseModel):
		directory: str
		
	
	@app.post("/directory")
	async def select_dir(dir: iRequest):
		print(dir.directory)

		w = open(".env", "w")
		w.write(f"{dir.directory}")
		w.close()
		
		return "Sucess"
	
# <-- Select CSV -->
	@app.get("/Select_csv")
	async def select_csv():
		r = open(".env", "r+")
		listfiles = r.read()
		listfiles = [file for file in os.listdir(listfiles) if file.endswith((".csv")) ]
		
		get_csv = []
		for x in listfiles:
			get_csv.append(x)
		return get_csv
except:
	path = readenv()
	path = "Any URL"
	
@app.get("/{fileName}")
async def read_csv(fileName):
	# <-- Reading Full CSV -->
	path = readenv()
	print(path)
	path_to_csv = f'{path}/{fileName}.csv'
	df = pd.read_csv(path_to_csv)
	df= df.to_json(orient='records')
	df = json.loads(df)
	return df

@app.get("/{fileName}/{Column}")
async def query(fileName, Column, value):
	# <-- Reading Specific CSV -->
	path = readenv()
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


app.mount(
	"/static",
	StaticFiles(directory=Path(__file__).parent.parent.absolute() / str(os.getcwd())),
	name="static",
)





@app.get("/")
async def Home(request: Request):
	return templates.TemplateResponse("layout.html", {
		"request": request
	})
	
	
def open_browser():
	webbrowser.open_new('http://127.0.0.1:8000/')
	
if __name__ == "__main__":
	import uvicorn
	Timer(1, open_browser).start();
	uvicorn.run(app, host="127.0.0.1", port=8000)
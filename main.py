import os
from fastapi import FastAPI
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR,'.env'))

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World","detail":"this is an api gateway/router"}

@app.get("/{path}")
async def router(path):
    return {"path":path}

    
import os
from fastapi import FastAPI,Form
from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

import requests


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR,'.env'))

app = FastAPI()

origins = [
    "http://172.18.0.1:5000",

    "http://127.0.0.1:9000",
    "http://127.0.0.1:9001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message":"Hello World","detail":"api-gateway"}

@app.get("/{path}")
async def router(path, payload:str=Form()):
    response = requests.get(os.getenv("INTERNALROUTERPATH"+"/route"),payload)
    return {"path":path}

@app.post("/{path}")
async def router(path):
    
    return {"path":path}

    
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import dotenv_values

config = dotenv_values("../.env" + (".production" if os.getenv("PROD") else ""))

app = FastAPI(root_path=config.get("FASTAPI_ROOT_PATH", None))

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/number/{number}")
def number_details(number: int):
    return {
        "number": number,
        "squared": number * number,
        "double": number * 2,
    }

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from config import settings
from db import get_session, Session, create_db_and_tables

app = FastAPI(root_path=settings.FASTAPI_ROOT_PATH)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}








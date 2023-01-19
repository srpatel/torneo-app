from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

app = FastAPI(root_path=settings.FASTAPI_ROOT_PATH)


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

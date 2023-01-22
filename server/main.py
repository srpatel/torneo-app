from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from config import settings
from db import get_session, Session, create_db_and_tables
from models.numbers import Divisor, DivisorDB, Number, NumberCreate, NumberDB

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


@app.get("/number/{number}", response_model=Optional[Number])
def number_details(number: int, session: Session = Depends(get_session)):
    return session.get(NumberDB, number)


@app.post("/number", response_model=Number)
def post_number(number: NumberCreate, session: Session = Depends(get_session)):
    input = number.dict(exclude_unset=True)
    n = input["number"]
    if not "divisors" in input:
        input["divisors"] = [
            DivisorDB(number=n, divisor=x) for x in range(1, n + 1) if n % x == 0
        ]
    if not "square" in input:
        input["square"] = n * n

    number_db = NumberDB(**input)

    session.add(number_db)
    session.commit()

    return number_db

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from sqlmodel import select

from config import settings
from db import get_session, Session, create_db_and_tables
from models import (
    TournamentRead,
    TournamentCreate,
    Tournament,
    TournamentOptions,
)

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


@app.get("/tournament", response_model=List[TournamentRead])
def get_tournaments(session: Session = Depends(get_session)):
    return session.exec(select(Tournament)).all()


@app.post("/tournament", response_model=TournamentRead)
def post_tournament(
    tournament: TournamentCreate, session: Session = Depends(get_session)
):
    t = Tournament.from_orm(tournament)
    if not t.name:
        raise HTTPException(status_code=400, detail="Tournament must have a name")
    session.add(t)
    session.commit()
    session.refresh(t)

    return t


@app.get("/tournament/{code}", response_model=TournamentRead)
def get_tournament(code: str, session: Session = Depends(get_session)):
    return session.exec(select(Tournament).where(Tournament.code == code)).one()


@app.delete("/tournament/{code}", response_model=TournamentRead)
def get_tournament(code: str, session: Session = Depends(get_session)):
    t = session.exec(select(Tournament).where(Tournament.code == code)).one()
    session.delete(t)
    session.commit()
    return t

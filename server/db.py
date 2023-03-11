from sqlmodel import SQLModel, Session, create_engine

from config import settings

engine_args = {"echo": settings.DEBUG}
if settings.DATABASE_URI.startswith("sqlite"):
    engine_args["connect_args"] = {"check_same_thread": False}
engine = create_engine(settings.DATABASE_URI, **engine_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

from config import settings
import db

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from sqlmodel import SQLModel, create_engine
import sqlalchemy
import alembic

from models.numbers import *

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = alembic.context.config

def run_migrations() -> None:
    """Run migrations
    """
    with db.engine.connect() as connection:
        alembic.context.configure(
            connection=connection, target_metadata=SQLModel.metadata
        )

        with alembic.context.begin_transaction():
            alembic.context.run_migrations()

run_migrations()

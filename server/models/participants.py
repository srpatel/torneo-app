from sqlmodel import Field

from models.commons import AutonumericId


class Participant(AutonumericId, table=True):
    __tablename__ = "participants"
    user_id: int = Field(nullable=False, foreign_key="users.id")
    tournament_id: int = Field(nullable=False, foreign_key="tournaments.id")
    # TODO: Score -> Hybrid property SQLAlchemy?

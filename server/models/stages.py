from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel

from models.commons import AutonumericId, IntID
from models.matches import Match

if TYPE_CHECKING:
    from models.matches import MatchRead
    from models.tournaments import Tournament, TournamentShort
    from models.users import User


class StageShort(SQLModel):
    stage: int


class StageBase(StageShort):
    tournament_id: int = Field(nullable=False, foreign_key="tournaments.id")


class StageWithTournament(IntID, StageBase):
    tournament: "TournamentShort"


class StageRead(StageWithTournament):
    matches: List["MatchRead"]


class Stage(AutonumericId, StageBase, table=True):
    __tablename__ = "stages"
    # Relationships
    matches: List[Match] = Relationship(back_populates="stage")
    tournament: Optional["Tournament"] = Relationship(back_populates="stages")

    def add_match(self, users: List["User"]) -> "Stage":
        self.create_match().add_players(users)
        return self

    def create_match(self) -> Match:
        return Match(stage=self)

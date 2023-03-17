from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import DateTime, Column
from sqlalchemy.sql import func

from models.commons import AutonumericId

if TYPE_CHECKING:
    from models.users import UserRead, User
    from models.stages import Stage, StageShort


class MatchPlayerBase(SQLModel):
    position: int
    result: Optional[int] = Field(default=None)


class MatchPlayer(AutonumericId, MatchPlayerBase, table=True):
    __tablename__ = "match_players"
    match_id: int = Field(nullable=False, foreign_key="matches.id")
    user_id: int = Field(nullable=False, foreign_key="users.id")

    # Relationships
    match: "Match" = Relationship(back_populates="players")
    user: "User" = Relationship()


class MatchPlayerRead(MatchPlayerBase):
    user: "UserRead"


class MatchBase(SQLModel):
    finished_at: Optional[datetime] = Field(default=None)
    
class MatchShort(MatchBase):
    pass


class Match(AutonumericId, MatchBase, table=True):
    __tablename__ = "matches"
    stage_id: int = Field(nullable=False, foreign_key="stages.id")
    started_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    # Relationships
    stage: "Stage" = Relationship(back_populates="matches")
    players: List["MatchPlayer"] = Relationship(back_populates="match")

    def add_players(self, players: List["User"]) -> "Match":
        """
        Add players to this match

        Parameters
        ----------
        players : List["User"]
            Ordered list of players. Each player's position is given by its index on the list.
        """
        for position, player in enumerate(players):
            self.players.append(MatchPlayer(user=player, position=position))
        return self


class MatchRead(MatchBase):
    stage: "StageShort"
    players: List[MatchPlayerRead]

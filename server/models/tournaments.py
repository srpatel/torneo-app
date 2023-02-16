from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import DateTime, Column
from sqlalchemy.sql import func
from models.participants import Participant
from models.stages import Stage

if TYPE_CHECKING:
    from models.stages import StageRead
    from models.users import User, UserRead

from models.utils import code_generator


class TournamentOptions(SQLModel):
    type: str
    rounds: Optional[int] = Field(default=None)
    timeRound: Optional[int] = Field(default=None)

    def __str__(self) -> str:
        return self.json(exclude_none=True)

    @classmethod
    def from_str(cls, s: str) -> "TournamentOptions":
        return TournamentOptions.parse_raw(s)


class TournamentBase(SQLModel):
    name: str
    finished_at: Optional[datetime] = Field(default=None)


class TournamentCreate(TournamentBase):
    options: TournamentOptions


class TournamentShort(TournamentBase):
    code: str
    created_at: datetime


class TournamentRead(TournamentCreate, TournamentShort):
    id: int
    stages: List["StageRead"]
    participants: List["UserRead"]


class Tournament(TournamentBase, table=True):
    __tablename__ = "tournaments"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    code: Optional[str] = Field(default_factory=code_generator, unique=True, index=True)

    # Relationships
    stages: List["Stage"] = Relationship(back_populates="tournament")
    participants: List["User"] = Relationship(
        back_populates="tournaments", link_model=Participant
    )

    # Options
    optionsJSON: str

    @property
    def options(self) -> TournamentOptions:
        return TournamentOptions.from_str(self.optionsJSON)

    def set_options(self, value: TournamentOptions):
        self.optionsJSON = str(value)

    @classmethod
    def from_orm(
        cls, obj: Any, update: Optional[Dict[str, Any]] = None
    ) -> "Tournament":
        if not update:
            update = {}
        if (
            not hasattr(obj, "optionsJSON")
            and hasattr(obj, "options")
            and isinstance(obj.options, TournamentOptions)
        ):
            update["optionsJSON"] = str(obj.options)
        return super().from_orm(obj, update)

    def add_participant(self, user: "User") -> "Tournament":
        self.participants.append(user)
        return self

    def add_participants(self, users: List["User"]) -> "Tournament":
        for u in users:
            self.add_participant(u)
        return self

    def create_stage(self, stage: int) -> "Stage":
        return Stage(stage=stage, tournament=self)

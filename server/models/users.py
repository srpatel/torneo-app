from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from models.participants import Participant
from models.matches import MatchPlayer

if TYPE_CHECKING:
    from models.tournaments import Tournament
    from models.matches import Match

from models.utils import code_generator


class UserBase(SQLModel):
    name: str


class User(UserBase, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    code: Optional[str] = Field(default_factory=code_generator, unique=True, index=True)

    tournaments: List["Tournament"] = Relationship(
        back_populates="participants", link_model=Participant
    )
    matches: List["Match"] = Relationship(
        link_model=MatchPlayer, sa_relationship_kwargs=dict(viewonly=True)
    )


class UserRead(UserBase):
    id: int


class UserWithCode(UserRead):
    code: str

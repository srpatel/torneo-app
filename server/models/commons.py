from typing import Optional
from sqlmodel import SQLModel, Field


class BaseModel(SQLModel):
    def __repr__(self):
        return f"{self.__class__.__name__}({str(self.dict())[1:-1]})"


class IntID(BaseModel):
    id: int


class OptionalIntID(BaseModel):
    id: Optional[int]


class AutonumericId(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)

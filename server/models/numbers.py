from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


# One need several models for each "object":
# - one for the DB representation
# - one for parsing get requests
# - one for parsing post requests


# Since Divisors are not posted, we don't need to have a create model.
class Divisor(SQLModel):
    divisor: int = Field(primary_key=True)


class DivisorDB(Divisor, table=True):
    __tablename__ = "divisors"
    number: int = Field(primary_key=True, foreign_key="numbers.number")


# Sometimes is convenient to have a base model for those attributes with shared definition across all the models
class NumberBase(SQLModel):
    number: int = Field(primary_key=True)
    square: int


# For the DB we want to specify the table name and the fact that divisors is a relationship between numbers and divisors. Type annotations define the types of columns in the DB automatically, althoug more can be specified using the Field()
class NumberDB(NumberBase, table=True):
    __tablename__ = "numbers"
    divisors: List[DivisorDB] = Relationship()
    # Since there is only one foreign key relating Number and Divisors, we don't need to specify anything else on the Relationship(). For more complex cases we can specify which foreign key use to set the relationship.


# This is for get requests, divisors are shown as Divisor so that `number` is not sent.
class Number(NumberBase):
    divisors: List[Divisor]


# When creating the Numbers, we might not want to specify the list of divisors on the post requests but rather let them be calculated. Since this model is going to be used by FastAPI to parse the post requests we need to say that divisors is optional by asigning a default value.
class NumberCreate(NumberBase):
    square: Optional[int] = None
    divisors: List[Divisor] = []

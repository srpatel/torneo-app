from typing import Dict, Type, TypeGuard

from sqlmodel import SQLModel

Model = Type[SQLModel]

references: Dict[str, Model] = {}


class ReferenceError(Exception):
    pass


def ismodel(val: type) -> TypeGuard[Model]:
    return issubclass(val, SQLModel)


def referentiable(cls: Model) -> Model:
    if not ismodel(cls):
        raise TypeError(f"TypeError: {cls} is not a model.")
    if cls.__name__ in references.keys():
        raise ReferenceError(
            f"ReferenceError: {cls.__name__} already added to references."
        )
    references[cls.__name__] = cls
    return cls

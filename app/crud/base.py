from pydantic import BaseModel
from typing import TypeVar, Generic, Type

from app.models.base import BaseClass

ModelType = TypeVar("ModelType", bound=BaseClass)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

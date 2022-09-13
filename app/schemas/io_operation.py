from pydantic import BaseModel


class IoOperationResult(BaseModel):
    data: str

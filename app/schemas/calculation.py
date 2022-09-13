from pydantic import BaseModel


class PrimeRequestInner(BaseModel):
    number: int


class PrimeRequest(BaseModel):
    data: PrimeRequestInner


class PrimeResponse(BaseModel):
    bool: bool

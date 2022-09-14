from pydantic import BaseModel


class CPURequestInner(BaseModel):
    number: int


class CPURequest(BaseModel):
    data: CPURequestInner


class CPUResponse(BaseModel):
    results: int

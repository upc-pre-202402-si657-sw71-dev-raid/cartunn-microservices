
from pydantic import BaseModel


class Order(BaseModel):
    name: str
    description: str
    code: int
    entryDate: str
    exitDate: str
    status: str
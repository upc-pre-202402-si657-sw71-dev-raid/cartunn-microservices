from pydantic import BaseModel


class TunningTask(BaseModel):
    modifiedPart: str
    date: str 
    status: str
from pydantic import BaseModel

class NotificationResource(BaseModel):
    orderId: int
    type: str
    description: str

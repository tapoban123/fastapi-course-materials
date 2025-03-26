from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NotificationCreate(BaseModel):
    user_id: str
    message: str
    
class NotificationRead(BaseModel):
    id: int
    user_id: str
    message: str
    created_at: datetime
    
    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import datetime
class ToDoListCreate(BaseModel):
    title:str
    status:str
    created_at:datetime

class ToDoListResponse(ToDoListCreate):
    id:int
    class Config:
        from_attributes=True
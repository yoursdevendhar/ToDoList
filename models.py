
from sqlalchemy import Column,Integer,String,DateTime
from database import Base
from datetime import datetime

class ToDoList(Base):
    __tablename__="todolist"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    status=Column(String(100),nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    
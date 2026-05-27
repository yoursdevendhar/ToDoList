
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import models
import schemas

from database import SessionLocal,engine

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/list")
def create_list(
    list:schemas.ToDoListCreate,
    db:Session=Depends(get_db)
):
    new_list=(models.ToDoList(
        title=list.title,
        status=list.status,
        created_at=datetime.utcnow()
    ))    
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list

@app.get("/list")
def get_list(
    db:Session=Depends(get_db)
):
    list=db.query(models.ToDoList).all()
    return list

@app.put("/list/{id}")
def update_list(
    id:int,
    list:schemas.ToDoListCreate,
    db:Session=Depends(get_db)
):
    new_list=(db.query(models.ToDoList)
    .filter(models.ToDoList.id==id)
    .first()
    )
    if not new_list:
        return {"message":"list not found"}
    new_list.title=list.title
    new_list.status=list.status
    new_list.created_at=datetime.utcnow()

    db.commit()
    db.refresh(new_list)
    return new_list

@app.delete("/list/{id}")
def delete_list(
    id:int,
    db:Session=Depends(get_db)
):
    list=(
        db.query(models.ToDoList)
        .filter(models.ToDoList.id==id)
        .first()
    )
    if not list:
        return {"message":"list not found"}
    else:
        db.delete(list)
    db.commit()   
    return {"message":"deleted successfully"}
 

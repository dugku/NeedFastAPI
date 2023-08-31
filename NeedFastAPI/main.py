from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import random

import models
from databases import engine, SessionLocal

models.Base.metadata.create_all(bind =engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

class Todo(BaseModel):
    task: str 
    due_date:str
    complete:bool = False
    
itemDict = {}

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return db.query(models.TaskQue).all()

@app.post("/todo/")
async def input_Todo(todo: Todo, db: Session = Depends(get_db)):
    taskEntry = models.TaskQue(
        String_Todo = todo.task,
        due_date = todo.due_date    
    )
    db.add(taskEntry)
    db.commit()
    return {'message': "Completed"} 
@app.get("/todo/{task}", )
async def get_todo(task:str ):
    if task in itemDict:
        return {"task": task, **itemDict[task]}
    else: 
        return {"error", "404 not found"}


@app.put("/complete/{task_id}")
async def complete_todo(task_id: int, db: Session = Depends(get_db)):
    taks_obj = db.query(models.TaskQue).filter(models.TaskQue.task_id == task_id).first()
    
    """setattr(taks_obj, "True", models.TaskQue.complete)"""
    return {"Does it work?": taks_obj}

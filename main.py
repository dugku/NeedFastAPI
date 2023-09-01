from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import update
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
async def complete_todo(task_id: int,todo: Todo ,db: Session = Depends(get_db)):
    change_complete = db.query(models.TaskQue).filter(models.TaskQue.task_id == task_id).update({"complete": True})

    if change_complete == None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.commit()
    return {"Does it work?": "Maybe"}

@app.delete('/delete/{task_id}')
async def delete_tas(task_id: int,db: Session = Depends(get_db)):
    change_complete = db.query(models.TaskQue).filter(models.TaskQue.task_id == task_id).delete()

    if change_complete == None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.commit()
    return{"message":"Deleted"}

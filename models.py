from sqlalchemy import Column, Integer, String, Boolean, DateTime

from databases import Base

class TaskQue(Base):
    __tablename__= "todo"

    task_id = Column(Integer, primary_key=True, index=True)
    String_Todo = Column(String)
    complete = Column(Boolean, default=False)
    due_date = Column(String)
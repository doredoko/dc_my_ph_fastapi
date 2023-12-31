from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Task(Base):
    __tablename__="task"
    
    id = Column(Integer,primary_key=True)
    title=Column(String(1024))
    #due_date=Column(Date)
    done = relationship("Done",back_populates="task",cascade="delete")
    
class Done(Base):
    __tablename__ = "done"
    
    id = Column(Integer,ForeignKey("task.id"),primary_key=True)
    task = relationship("Task",back_populates="done")
    
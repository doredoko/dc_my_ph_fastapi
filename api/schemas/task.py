from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title: str | None = Field( None, example =f" クリーニング を 取り に 行く")
    
class TaskCreate(TaskBase):
    pass

class TaskCreateResponce(TaskBase):
    id: int

    class Config:
        #orm_mode=True
        from_attributes = True
class Task(TaskBase):
    id: int
    done: bool = Field(False,description="完了フラグ")
    
    class Config:
        #orm_mode=True
        from_attributes = True

from fastapi import APIRouter,Depends,HTTPException
import api.schemas.task as task_schema
from sqlalchemy.orm import Session
import api.cruds.task as task_croud
from api.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.get("/task",response_model = list[task_schema. Task])
async def list_task(db: AsyncSession=Depends(get_db)):
    return await task_croud.get_task_with_done(db)

@router.post("/task",response_model=task_schema.TaskCreateResponce)
async def create_task(task_body: task_schema.TaskCreate,db: AsyncSession = Depends(get_db)):
    return await task_croud.create_task(db,task_body)

@router.put("/task/{task_id}",response_model=task_schema.TaskCreateResponce)
async def update_task(task_id:int,task_body:task_schema.TaskCreate,db:AsyncSession=Depends(get_db)):
    task=await task_croud.get_task(db,task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await task_croud.update_task(db,task_body,original=task)

@router.delete("/task/{task_id}",response_model=None)
async def delete_task(task_id: int,db: AsyncSession=Depends(get_db)):
    task=await task_croud.get_task(db,task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return await task_croud.delete_task(db,original=task)
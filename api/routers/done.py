from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.task as task_croud
from api.db import get_db
import api.cruds.done as done_crud

router = APIRouter()

@router.put("/task/{task_id}/done",response_model=None)
async def mark_task_as_done(task_id:int,db:AsyncSession=Depends(get_db)):
    done = await done_crud.get_done(db,task_id=task_id)
    if done is None:
        raise HTTPException(status_code=400,detail="Done already exists")


@router.delete("/task/{task_id}/done",response_model=None)
async def unmark_task_as_done(task_id: int, db: AsyncSession=Depends(get_db)):
    done=await done_crud.get_done(db,task_id=task_id)
    if done is None:
        raise HTTPException(statuscode=404,detail="Done not found")
    return await done_crud.delete_done(db,original=done)



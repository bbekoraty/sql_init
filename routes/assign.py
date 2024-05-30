from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain import schemas, crud, database, geo_sort
from typing import List

router = APIRouter(
    prefix="/assign",
    tags=["assign"],
    responses={404: {"description": "Not found"}},
)

@router.get("/id/{assign_id}", response_model=schemas.AssignResponse)
def read_assign(assign_id: int, db: Session = Depends(database.get_db)):
    get_assign = crud.get_assign(db=db, assign_id=assign_id)
    if get_assign is None:
        raise HTTPException(status_code=404, detail="Assign not found")
    return get_assign

@router.get("/all", response_model=List[schemas.AssignResponse])
def read_assigns(db: Session = Depends(database.get_db)):
    assigns = crud.get_assigns(db=db)
    if assigns is None:
        raise HTTPException(status_code=404, detail="Assign not found")
    return assigns


@router.post("/create", response_model=schemas.AssignResponse)
def create_job(job: schemas.AssignCreate, db: Session = Depends(database.get_db)):
    return crud.create_assign(db=db, list=job)

@router.delete("/assigns/{assign_id}", response_model=schemas.AssignResponse)
def delete_assign(assign_id: int, db: Session = Depends(database.get_db)):
    db_assign = crud.delete_assign(db, assign_id=assign_id)
    if db_assign is None:
        raise HTTPException(status_code=404, detail="Assign not found")
    return db_assign

@router.put("/assigns/{assign_id}", response_model=schemas.AssignResponse)
def update_assign(assign_id: int, assign: schemas.AssignCreate, db: Session = Depends(database.get_db)):
    db_assign = crud.update_assign(db, assign_id=assign_id, assign=assign)
    if db_assign is None:
        raise HTTPException(status_code=404, detail="Assign not found")
    return db_assign

@router.post("/clone_to_assign/", response_model=list[schemas.AssignResponse])
def copy_jobs_to_assigns(db: Session = Depends(database.get_db)):
    jobs = crud.get_Jobs(db)
    assigns = []
    for job in jobs:
        new_assign = schemas.AssignCreate(
            job_id=job.id,
            project=job.project,
            hotspot_type=job.hotspot_type,
            max_temp=job.max_temp,
            string_tag=job.string_tag,
            priority=job.priority,
            header='',  
            worker='',
            status=''
        )
        assigns.append(crud.create_assign(db=db, assign=new_assign))
    return assigns



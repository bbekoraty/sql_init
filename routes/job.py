from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain import schemas, crud, database, geo_sort
from typing import List

router = APIRouter(
    prefix="/job",
    tags=["job"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(database.get_db)):
    return crud.create_Job(db=db, list=job)

@router.post("/upload/")
async def upload_job(data: schemas.FeatureCollection):
    return {"received_data": data}

@router.post("/commit/", response_model=list[schemas.Job])
async def commit_job(data: schemas.FeatureCollection, db: Session = Depends(database.get_db)):
    try:
        processed_data = geo_sort.Data01(data.dict())
        if not processed_data:
            raise HTTPException(status_code=400, detail="No data processed")
        db_items = []
        for item in processed_data:
            try:
                list_item = schemas.JobCreate(
                    project=item['Project'],
                    hotspot_type=item['hotspot_type'],
                    max_temp=item['Max Temperature'],
                    string_tag=item['string_tag'],
                    priority=item['priority']
                )
                db_item = crud.create_Job(db=db, list=list_item)
                db_items.append(db_item)
            except Exception as e:
                print(f"Error processing item: {item}")
                print(f"Exception: {e}")
                raise HTTPException(status_code=500, detail="Error inserting data into database")
        return db_items
    except Exception as e:
        print(f"Error processing data: {e}")
        raise HTTPException(status_code=400, detail="Error processing data")

@router.get("/get", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, db: Session = Depends(database.get_db)):
    jobs = crud.get_Jobs(db=db, skip=skip)
    return jobs

@router.get("/{job_id}", response_model=schemas.Job)
def read_job(job_id: int, db: Session = Depends(database.get_db)):
    db_job = crud.get_Job(db=db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job
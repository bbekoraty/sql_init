from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from domain import crud , database, schemas

router = APIRouter(
    prefix="/man",
    tags=["man"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ManResponse)
def create_man(man: schemas.ManCreate, db: Session = Depends(database.get_db)):
    return crud.create_man(db=db, man=man)

@router.get("/", response_model=List[schemas.ManResponse])
def get_mens(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    men = crud.get_lsman(db=db, skip=skip, limit=limit)
    return men

@router.get("/{man_id}", response_model=schemas.ManResponse)
def get_man(man_id: int, db: Session = Depends(database.get_db)):
    db_man = crud.get_man(db=db, man_id=man_id)
    if db_man is None:
        raise HTTPException(status_code=404, detail="Man not found")
    return db_man

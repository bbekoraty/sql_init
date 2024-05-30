from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domain import database , crud
router = APIRouter()

@router.post("/create_database/")
def create_db(db_name: str, session: Session = Depends(database.get_db)):
    return crud.create_database(session, db_name)

@router.get("/list_databases/")
def list_dbs(session: Session = Depends(database.get_db)):
    return crud.list_databases(session)
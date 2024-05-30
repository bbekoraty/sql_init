from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models, schemas
from fastapi import HTTPException

##JOB SECTION##
def create_Job(db: Session, list: schemas.JobCreate):
    db_list = models.Job(
        project=list.project,
        hotspot_type=list.hotspot_type,
        max_temp=list.max_temp,
        string_tag=list.string_tag,
        priority = list.priority
    )
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def get_Jobs(db: Session, skip: int = 0):
    return db.query(models.Job).offset(skip).all()

def get_Job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

##MAN SECTION##
def create_man(db: Session, man: schemas.ManCreate):
    db_man = models.Man(**man.dict())
    db.add(db_man)
    db.commit()
    db.refresh(db_man)
    return db_man

def get_man(db: Session, man_id: int):
    return db.query(models.Man).filter(models.Man.id == man_id).first()

def get_lsman(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Man).offset(skip).limit(limit).all()

##Assign table
def get_assign(db: Session, assign_id: int):
    return db.query(models.Assign).filter(models.Assign.job_id == assign_id).first()

def get_assigns(db: Session, skip: int = 0):
    return db.query(models.Assign).offset(skip).all()

def create_assign(db: Session, assign: schemas.AssignCreate):
    db_assign = models.Assign(**assign.dict())
    db.add(db_assign)
    db.commit()
    db.refresh(db_assign)
    return db_assign

def delete_assign(db: Session, assign_id: int):
    db_assign = db.query(models.Assign).filter(models.Assign.id == assign_id).first()
    if db_assign:
        db.delete(db_assign)
        db.commit()
    return db_assign

def update_assign(db: Session, assign_id: int, assign: schemas.AssignCreate):
    db_assign = db.query(models.Assign).filter(models.Assign.id == assign_id).first()
    if db_assign:
        for key, value in assign.dict().items():
            setattr(db_assign, key, value)
        db.commit()
        db.refresh(db_assign)
    return db_assign

##db
def create_database(session: Session, db_name: str):
    try:
        session.connection().connection.set_isolation_level(0)  # set autocommit mode
        session.execute(text(f"CREATE DATABASE {db_name}"))
        session.connection().connection.set_isolation_level(1)  # reset isolation level
        return {"message": f"Database {db_name} created successfully."}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

def list_databases(session: Session):
    try:
        result = session.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false"))
        databases = [row[0] for row in result]
        return {"databases": databases}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

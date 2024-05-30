from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from domain import models
from domain import database


from routes import job,man,db,assign

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job.router)
app.include_router(man.router)
app.include_router(assign.router)
app.include_router(db.router)

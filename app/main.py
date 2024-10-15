from fastapi import FastAPI
from app import models, database, crud
from app.schemas import AccessLogCreate

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "Welcome To The Access Log API"}

@app.get("/logs/")
def get_logs():
    return crud.get_logs(database.SessionLocal())

@app.post("/logs/")
def add_log(log: AccessLogCreate):
    return crud.add_log(log, database.SessionLocal())


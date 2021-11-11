from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/jobs/',response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_user = crud.get_job_by_link(db, job_link=job.link)
    if db_user:
        raise HTTPException(status_code=400,detail="Link already in database")
    return crud.create_job(db=db,job=job)

@app.get('/jobs/all')
def get_all_jobs(db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db,0,100)
    if len(jobs) == 0:
        return {'no jobs':'sorry!'}
    return crud.get_jobs(db,0,100)


from sqlalchemy.orm import Session

import models, schemas

def get_job(db: Session, job_id:int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def create_job(db: Session, job:schemas.JobCreate):
    db_job = models.Job(link=job.link)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_job_by_link(db:Session, job_link:str):
    return db.query(models.Job).filter(models.Job.link == job_link).first()
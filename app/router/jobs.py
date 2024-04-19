from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List


from ..oauth2 import get_current_user

from ..services.url_to_job_info_service import job_info_from_url

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/jobs",
    tags=['Jobs']
)

@router.post("/add", response_model=schemas.JobInfo, status_code=status.HTTP_201_CREATED)
async def add_job(job_url: schemas.JobUrlToAdd, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """ add of a job post """
    jobinfo = job_info_from_url(job_url.url)

    job_info = {
                    "job_title":jobinfo.job_title,
                    "job_description":jobinfo.job_description,
                    "company_name":jobinfo.company_name,
                    "location":jobinfo.location}
    job_to_db = job_info
    job_to_db["owner_id"] = current_user.id
    job_to_db["applied"] = False
    
    job_to_add = models.Jobs(**job_info)
    db.add(job_to_add)
    db.commit()
    db.refresh(job_to_add)

    return job_info

@router.get("/getAll", response_model=List[schemas.JobInfo], status_code=status.HTTP_200_OK)
async def get_jobs(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    jobs = db.query(models.Jobs).filter(models.Jobs.owner_id == current_user.id).all()
    return jobs

@router.post("/update_applied", response_model=schemas.JobInfo, status_code=status.HTTP_202_ACCEPTED)
async def add_job(job_data: schemas.UpdateJobById, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """ update appied status """
    jobinfo = db.query(models.Jobs).filter(models.Jobs.id == job_data.id and models.Jobs.owner_id == current_user.id).first()

    if jobinfo is None:
        raise HTTPException(status_code=404, detail="Item not found")

    jobinfo.applied = job_data.applied

    jobinfo.applied = job_data.applied
    db.commit()
    
    return jobinfo
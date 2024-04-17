from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

from ..services.url_to_job_info_service import job_info_from_url

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/jobs",
    tags=['Jobs']
)

@router.post("/add", response_model=schemas.JobInfo, status_code=status.HTTP_201_CREATED)
async def add_job(job_url: schemas.JobUrlToAdd, db: Session = Depends(get_db)):
    """ add of a user """
    jobinfo = job_info_from_url(job_url.url)
    return {"job_id":1,
            "job_title":jobinfo.job_title,
            "job_description":jobinfo.job_description,
            "company_name":jobinfo.company_name,
            "location":jobinfo.location}
"""
Pydantic Models are used as Schema Validation
for request and responses parameters
"""
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

from datetime import datetime

from sqlalchemy import TIMESTAMP


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr  # from pydantic
    created_at: datetime

    class Config():
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int]


class JobInfo(BaseModel):
    id:int = 0
    job_title:str
    job_description:str
    company_name:str
    location:str
    applied:bool = False
    created_at: Optional[datetime] = datetime.now()

class JobUrlToAdd(BaseModel):
    url:str

class UpdateJobById(BaseModel):
    id:int
    applied:bool

class ScrapedJobInfo:
    def __init__(self, title, desc, comapany, location) -> None:
        self.job_title = title
        self.job_description = desc
        self.company_name = comapany
        self.location = location
        pass
    job_title:str
    job_description:str
    company_name:str
    location:str
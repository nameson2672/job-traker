"""
Main Application File for our FastApi Server
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .router import auth, user, jobs

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://www.google.com",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(jobs.router)


@ app.get("/")
async def root():
    return {"message": "This is the main page"}


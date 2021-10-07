from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

"""
username
email
created_at

"""
class User(BaseModel):
    username: str
    email: str

@app.get("/")
async def read_root():
    return {"cocktail": "app"}

@app.get("/boozes")
async def read_root():
    return {"booze": "here"}

@app.get("/users")
async def read_root():
    return {"users": "here"}

@app.post("/users")
async def create_user(user: User):
    return user
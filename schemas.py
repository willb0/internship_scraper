from typing import List, Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    link: str


class JobCreate(BaseModel):
    link: str


class Job(BaseModel):
    id: int
    link: str

    class Config:
        orm_mode = True

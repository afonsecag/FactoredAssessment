from pydantic import BaseModel
from typing import List

class Skill(BaseModel):
    skill: str
    score: int
class UserProfile(BaseModel):
    nombre: str
    email: str
    position: str
    skills: List[Skill]
    avatar_url: str

class Employee(BaseModel):
    id: int
    name: str
    email: str
    password: str
    position: str
    skills: List[Skill]
    avatar_url: str
    
    class Config:
        orm_mode = True


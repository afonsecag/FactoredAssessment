from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from app.schemas import employee as employee_schema
from app.database.db import SessionLocal
from app.models.employee import Employee as EmployeeModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Cookie, Depends, Response, Request
from app.schemas.employee import UserProfile
import json


app = FastAPI()

Base = declarative_base()

origins = [
    "http://localhost:3000",  # React frontend local address
]

# Añadir middleware para manejar CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la sesión de la base de datos
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/employee/{employee_id}", response_model=employee_schema.Employee)
async def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    db_employee.skills = json.loads(db_employee.skills)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.post("/login/")
def login(response: Response, request: LoginRequest, db: Session = Depends(get_db)):
    email = request.email
    password = request.password
    db_user = db.query(EmployeeModel).filter(EmployeeModel.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if password != db_user.password:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    
    return {"message": "Inicio de sesión exitoso"}


@app.get("/profile", response_model=UserProfile)
async def get_profile_data(db: Session = Depends(get_db)):

    user_id = 1 

    db_user = db.query(EmployeeModel).filter(EmployeeModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    skills_list = json.loads(db_user.skills) if isinstance(db_user.skills, str) else db_user.skills

    user_profile = UserProfile(
        nombre=db_user.name, 
        email=db_user.email,
        position=db_user.position,  
        skills=skills_list,
        avatar_url=db_user.avatar_url  
    )
    
    return user_profile
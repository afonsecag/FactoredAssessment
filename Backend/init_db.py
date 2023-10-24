import hashlib
from sqlalchemy.orm import Session
from app.database.db import SessionLocal, engine
from app.models.employee import Base, Employee
import json

def get_gravatar_url(email):
    email = email.lower().strip()
    hash = hashlib.md5(email.encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{hash}"
    return url

Base.metadata.create_all(bind=engine)
db = SessionLocal()

new_employee = Employee(
    name="John Doe",
    email="johndoe@gmail.com",
    password="johndoe",
    position="Software Developer",
    skills=json.dumps([{"skill": "Python", "score": 80}, {"skill": "SQL", "score": 70}, {"skill": "Java", "score": 50}, {"skill": "JavaScript", "score": 60}, {"skill": "React", "score": 90}]),
    avatar_url=get_gravatar_url("john.doe@example.com")
)

db.add(new_employee)
db.commit()
db.close()
print("Usuario añadido correctamente!")

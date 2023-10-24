from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    position = Column(String)
    skills = Column(String)
    avatar_url = Column(String)

    @property
    def skills_as_object(self):
        return json.loads(self.skills)
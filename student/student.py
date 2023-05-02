# Hier leigt Bussiness Logic
from pydantic import BaseModel, EmailStr
from typing import Optional,List

class CourseModel(BaseModel):
    name: str

class StudentModel(BaseModel):
    name: str
    email: EmailStr
    uni: Optional[str]
    telnum: Optional[str]
    address: Optional[str]
    birth_date: Optional[str]
    courses: Optional[CourseModel]

def create_student(new_student:StudentModel,fake_db={}):
    pk = len(fake_db)
    fake_db[pk]=new_student
    if fake_db.get(pk):
        return True
    return False

def read_student(id:str,fake_db={})-> StudentModel | None:
    if fake_db.get(id):
        return fake_db.get(id)
    return None
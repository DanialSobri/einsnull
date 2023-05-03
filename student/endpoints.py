#  Hier liegt following endpoints:
#  GET student/{id} : Return all student info in JSON format
#  POST student/update/{id}
#  DELETE student/{id}
#  POST student/{id}/addcourse/{courseinfo}
#  GET student/courses/   : Return all courses per student [ JSON ]

from faker import Faker
from fastapi import APIRouter, HTTPException
from config import settings
from student.student import StudentModel
from pydantic import BaseModel, EmailStr
from typing import Optional,List

router = APIRouter(
    prefix="{}/student".format(settings.API_V1_STR),
    tags=["student"],
    responses={404: {"description":"Not found"}}
    )

# Fake DB
db = {}
fake = Faker()

# A Pydantic model to validate the item data
class Student(BaseModel):
    id:int
    name: str
    email: EmailStr
    uni: Optional[str]
    telnum: Optional[str]
    address: Optional[str]
    birth_date: Optional[str]
    courses: Optional[list]

# A helper function to generate a new item with fake data
def create_new_student():
    return Student(
        id = len(db) + 1,
        name = fake.name(),
        email = fake.email(),
        telnum = fake.msisdn()
    )

# CRUD Student
# Read all items in the database
@router.get("/all")
async def get_all_students():
    return list(db.values())

# Read an item by id
@router.get("/{student_id}",response_model=Student)
async def get_student(student_id:int):
    if student_id in db:
        return db.get(student_id)
    raise HTTPException(status_code=404, detail="Item not found")

# Create a new item and add it to the database
@router.post("/create/", response_model=Student)
def create_student():
    student = create_new_student()
    db[student.id] = student
    return student

# Update an item by id
@router.put("/update/{student_id}",response_model=Student)
async def update_student(student_id:int, student:Student):
    if student_id in db:
        db[student_id] = student
        return student
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item by id
@router.delete("/{student_id}")
async def delete_student(student_id:int):
    if student_id in db:
        del db[student_id]
        return None
    raise HTTPException(status_code=404, detail="Item not found")

# CRUD courses
@router.post("/{id}/addcourse/{courseinfo}")
async def add_student_course():
    return {"message": "Hello World"}

@router.get("/courses/")
async def get_student_courses():
    return {"message": "Hello World"}
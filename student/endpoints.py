#  Hier liegt following endpoints:
from fastapi import APIRouter, HTTPException
from config import settings
from student.student import Student,Course, create_new_student, generate_fake_student, create_new_course
import logging

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

router = APIRouter(
    prefix="{}/student".format(settings.API_V1_STR),
    tags=["student"],
    responses={404: {"description":"Not found"}}
    )

# Fake DB
db = {}
if settings.FAKE:
    # Tabulate fake data
    generate_fake_student(5,db,logger)

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
    student = create_new_student(db)
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
@router.post("/{student_id}/addcourse",response_model=Student)
async def add_student_course(student_id:int):
    if student_id in db:
        student = db.get(student_id)
        new_course = create_new_course(student.courses)
        student.courses[new_course.id] = new_course
        return student
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/courses/{student_id}")
async def get_student_courses(student_id:int):
    if student_id in db:
        student = db.get(student_id)
        logger.info(type(student))
        return student.courses
    raise HTTPException(status_code=404, detail="Item not found")
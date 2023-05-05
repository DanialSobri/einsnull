# Hier leigt Bussiness Logic
from pydantic import BaseModel, EmailStr
from typing import Optional,List
from faker import Faker

fake = Faker()

# A Pydantic model to validate the item data
class Student(BaseModel):
    id:int
    name: str
    email: EmailStr
    telnum: Optional[str]
    address: Optional[str]
    birth_date: Optional[str]
    courses: Optional[dict]

class Course(BaseModel):
    id:int
    name: str
    slug: str
    institution: str
    level: str
    spo: Optional[str]
    startdate: Optional[str]

# A helper function to generate a new item with fake data
def create_new_student(db):
    return Student(
        id = len(db) + 1,
        name = fake.name(),
        email = fake.email(),
        telnum = fake.msisdn(),
        courses = {}
    )

def create_new_course(db):
    return Course(
        id = len(db) + 1,
        name = "Technische Informatik",
        slug = "B.Eng",
        institution = "HS Augsburg",
        level = "Bachelor"
    )

def generate_fake_student(total_fake_acc,db,logger):
    # Tabulate fake data
    logger.info("Tabulate fake db.")
    for _ in range(total_fake_acc):
        student = create_new_student(db)
        db[student.id] = student
    logger.info("{} fake students available in db.".format(len(list(db.values()))))

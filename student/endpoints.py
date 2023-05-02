#  Hier liegt following endpoints:
#  GET student/{id} : Return all student info in JSON format
#  POST student/update/{id}
#  DELETE student/{id}
#  POST student/{id}/addcourse/{courseinfo}
#  GET student/courses/   : Return all courses per student [ JSON ]


from fastapi import APIRouter
from config import settings

router = APIRouter(
    prefix="{}/student".format(settings.API_V1_STR),
    tags=["student"],
    responses={404: {"description":"Not found"}}
    )

@router.get("/all")
async def get_all_students():
    return {"message": "Hello World"}

@router.get("/{id}")
async def get_student():
    return {"message": "Hello World"}

@router.post("/update/{id}")
async def update_student():
    return {"message": "Hello World"}

@router.delete("/{id}")
async def delete_student():
    return {"message": "Hello World"}

@router.post("/{id}/addcourse/{courseinfo}")
async def add_student_course():
    return {"message": "Hello World"}

@router.get("/courses/")
async def get_student_courses():
    return {"message": "Hello World"}
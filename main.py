from fastapi import FastAPI,APIRouter

# /api/v1/student
# student
import student
from config import settings

router = APIRouter(prefix="{}".format(settings.API_V1_STR),
                   tags=["core"]
                   )

@router.get("/")
async def hello():
    return {"message": "Hello World"}

app = FastAPI()

app.include_router(router)
app.include_router(student.router)
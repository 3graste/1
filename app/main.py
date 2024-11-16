from fastapi import FastAPI, APIRouter
from routers import user
from routers import task

app = FastAPI()

router = APIRouter()

@router.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)
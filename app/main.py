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

from db import engine
from models import Base

# Создаем все таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Выводим SQL-запросы
print(Base.metadata.create_all(bind=engine))

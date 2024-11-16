from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# Создаем движок базы данных
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# Создаем локальную сессию
SessionLocal = sessionmaker(bind=engine)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

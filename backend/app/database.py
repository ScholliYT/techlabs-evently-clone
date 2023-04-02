from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from . import models, schemas


SQLALCHEMY_DATABASE_URL = "sqlite:///./events.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="utf-8-sig", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
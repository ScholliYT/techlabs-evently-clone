from sqlalchemy import Column, Integer, String
from app.database import Base
from typing import Optional
from pydantic import BaseModel



class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    objektart = Column(String)
    name = Column(String)
    link = Column(String)
    address = Column(String)

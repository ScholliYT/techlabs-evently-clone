from typing import List, Optional
from pydantic import BaseModel


class EventBase(BaseModel):
    objektart: str
    name: str
    link: str
    address: str
    image_url: Optional[str] = None  


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
        
        
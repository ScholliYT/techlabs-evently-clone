from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas


from sqlalchemy.orm import Session
from app import models, schemas


def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def update_event(db: Session, event: schemas.Event, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    for var, value in vars(event).items():
        setattr(db_event, var, value) if value else None
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    db.delete(db_event)
    db.commit()
    return db_event


def get_event_by_name_and_address(db: Session, name: str, address: str):
    return db.query(models.Event).filter(models.Event.name == name, models.Event.address == address).first()
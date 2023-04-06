from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from . import schemas, crud, database

router = APIRouter()


@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(database.get_db)):
    db_event = crud.create_event(db=db, event=event)
    return db_event

@router.get("/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 5000, db: Session = Depends(database.get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events

@router.get("/{event_id}", response_model=schemas.Event)
def read_event(event_id: int, db: Session = Depends(database.get_db)):
    db_event = crud.get_event(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    html_content = f"""
    <html>
        <head>
            <title>{db_event.name}</title>
        </head>
        <body>
            <h1>{db_event.name}</h1>
            <img src="{db_event.image_url}" alt="{db_event.name}">
            <p>{db_event.address}</p>
            <a href="{db_event.link}">{db_event.link}</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@router.put("/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(database.get_db)):
    db_event = crud.get_event(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db_event = crud.update_event(db=db, event=event, event_id=event_id)
    return db_event

@router.delete("/{event_id}", response_model=schemas.Event)
def delete_event(event_id: int, db: Session = Depends(database.get_db)):
    db_event = crud.get_event(db=db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db_event = crud.delete_event(db=db, event_id=event_id)
    return db_event
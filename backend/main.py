import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app import event, database, models, schemas, crud
import csv
import pandas as pd

app = FastAPI()

from config import settings

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Load the data from the CSV file and store it in the database
def load_csv_data():
    existing_event_names = []
    with open("C:/Users/maxwe/Documents/EventlyTechLabs/evently/better_data_file2.csv", encoding="utf-8-sig") as f: # Modify this line to your current directory
        reader = csv.reader(f)
        reader = csv.reader(f)
        next(reader)  # skip header row
        events = [schemas.EventCreate(objektart=row[1], name=row[2], link=row[3], address=row[4], image_url=row[5]) for row in reader]
        with database.SessionLocal() as db:
            existing_events = set(db.query(models.Event.name, models.Event.address).all())
            new_events = []
            duplicate_events = []
            for event in events:
                # check if event already exists in database
                if (event.name, event.address) in existing_events:
                    duplicate_events.append(event)
                else:
                    new_events.append(event)
            # create new events
            for event in new_events:
                crud.create_event(db=db, event=event)
            

# Load the data from the CSV file and store it in the database when the application starts
load_csv_data()

app.include_router(event.router, prefix="/event")

# Serve the static files
app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
# app.mount("/create", StaticFiles(directory="../frontend", html=True), name="create")

# Setup cors - to allow cross origin requests (e.g. from different hostnames)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level=settings.DEBUG,
        workers=settings.WORKERS,
    )
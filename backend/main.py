from fastapi import FastAPI
from app import event, database, models, schemas, crud
import csv

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Load the data from the CSV file and store it in the database
def load_csv_data():
    with open("/Users/laura/Course_TechLabs/evently_2/evently/better_data_file.csv") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        events = [schemas.EventCreate(objektart=row[1], name=row[2], link=row[3], address=row[4]) for row in reader]
        with database.SessionLocal() as db:
            for event in events:
                crud.create_event(db=db, event=event)

# Load the data from the CSV file and store it in the database when the application starts
load_csv_data()

app.include_router(event.router)

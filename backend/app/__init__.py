from fastapi import FastAPI

app = FastAPI()

from app import crud, models, schemas, database, event
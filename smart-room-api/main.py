from fastapi import FastAPI, Depends
import models
from database import engine
from routers import sensors

models.Base.metadata.create_all(bind=engine)#this line just creates the database tables if they dont exist

app = FastAPI()

app.include_router(sensors.router)

@app.get("/ping")
async def ping():
    return{"message": "pong!"}

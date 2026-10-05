from fastapi import FastAPI, Depends
import schemas
import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)#this line just creates the database tables if they dont exist

app = FastAPI()

#dependency: opens a database session and closes it when the request is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ping")
async def ping():
    return{"message": "pong!"}

@app.post("/data")
async def receive_data(data: schemas.SensorData, db: Session = Depends(get_db)):
    #creates a new database record using the model from models.py
    db_record = models.SensorRecord(
        temperature=data.temperature
    )

    db.add(db_record)#add changes
    db.commit()#save changes
    db.refresh(db_record) # Get the newly generated ID

    print(f"Received: record_id={db_record.id} Temp={data.temperature}ºC")

    #return a success message
    return {
        "status": "success", 
        "message": "Data saved to database!", 
        "record_id": db_record.id
    }
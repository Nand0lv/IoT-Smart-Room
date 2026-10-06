from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
from database import SessionLocal
from typing import List

router = APIRouter()

#dependency: opens a database session and closes it when the request is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/data")
async def receive_data(data: schemas.SensorData, db: Session = Depends(get_db)):
    #using CRUD function to create a sensor record
    new_record = crud.create_sensor_record(db=db, data=data)
    
    return {
        "status": "success", 
        "message": "Data saved successfully!", 
        "record_id": new_record.id
    }

#the response will be a List of SensorResponse schema
@router.get("/data", response_model=List[schemas.SensorResponse])
async def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = crud.get_sensor_records(db, skip=skip, limit=limit)
    return records
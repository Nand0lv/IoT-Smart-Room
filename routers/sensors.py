from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
from database import SessionLocal

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
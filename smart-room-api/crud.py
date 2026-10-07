from sqlalchemy.orm import Session
import models
import schemas

def create_sensor_record(db: Session, data: schemas.SensorData):
    #creates a new database record using the model from models.py
    db_record = models.SensorRecord(
        temperature=data.temperature,
        humidity= data.humidity
    )
    db.add(db_record)#add changes
    db.commit()#save changes
    db.refresh(db_record)#get the newly generated ID
    return db_record

def get_sensor_records(db: Session, skip: int = 0, limit: int = 100):
    #offset(skip) and limit(limit) are used for pagination to prevent memory overload
    return db.query(models.SensorRecord).offset(skip).limit(limit).all()
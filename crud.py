from sqlalchemy.orm import Session
import models
import schemas

def create_sensor_record(db: Session, data: schemas.SensorData):
    #creates a new database record using the model from models.py
    db_record = models.SensorRecord(
        temperature=data.temperature
    )
    db.add(db_record)#add changes
    db.commit()#save changes
    db.refresh(db_record)#get the newly generated ID
    return db_record
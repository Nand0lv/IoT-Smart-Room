from sqlalchemy import Column, Integer, Float, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class SensorRecord(Base):
    __tablename__ = "sensor_records"

    #Columns
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    timestamp = Column(DateTime, default=func.now()) #records when it was saved
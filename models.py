from sqlalchemy import Column, Integer, Float, Boolean, DateTime
from database import Base
import datetime

class SensorRecord(Base):
    __tablename__ = "sensor_records"

    #Columns
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc)) #records when it was saved
from pydantic import BaseModel
from datetime import datetime

#this is the information that we get from ESP-32
class SensorData(BaseModel):
    temperature: float

class SensorResponse(SensorData):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  #allows pydantic to read db objects
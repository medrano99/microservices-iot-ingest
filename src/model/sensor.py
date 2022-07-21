from typing import Optional
from pydantic import BaseModel

class Sensor(BaseModel):
    id:Optional[str]
    id_device: str
    temperature:int
    timestamp: int


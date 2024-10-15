from pydantic import BaseModel
from datetime import datetime

class AccessLogCreate(BaseModel):
    fingerprint_hash: str

class AccessLog(BaseModel):
    id: int
    fingerprint_hash: str
    access_time: datetime

    class Config:
        from_attributes = True

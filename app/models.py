from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AccessLog(Base):
    __tablename__ = 'access_logs'
    id = Column(Integer, primary_key=True, index=True)
    fingerprint_hash = Column(String, index=True)
    access_time = Column(DateTime, default=datetime.astimezone)

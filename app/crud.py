from app.models import AccessLog
from sqlalchemy.orm import Session
from app.schemas import AccessLogCreate

def get_logs(db: Session):
    return db.query(AccessLog).all()

def add_log(log: AccessLogCreate, db: Session):
    db_log = AccessLog(fingerprint_hash=log.fingerprint_hash)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

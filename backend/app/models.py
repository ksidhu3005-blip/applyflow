import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Enum
from app.database import Base


class StatusEnum(str, enum.Enum):
    applied = "Applied"
    interview = "Interview"
    offer = "Offer"
    rejected = "Rejected"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.applied, nullable=False)
    date_applied = Column(Date)
    notes = Column(Text, nullable=True)
    link = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

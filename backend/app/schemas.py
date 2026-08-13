from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from app.models import StatusEnum


class ApplicationBase(BaseModel):
    company: str
    role: str
    status: StatusEnum = StatusEnum.applied
    date_applied: Optional[date] = None
    notes: Optional[str] = None
    link: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[StatusEnum] = None
    date_applied: Optional[date] = None
    notes: Optional[str] = None
    link: Optional[str] = None


class ApplicationOut(ApplicationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

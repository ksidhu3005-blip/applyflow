from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Application, StatusEnum
from app.schemas import ApplicationCreate, ApplicationUpdate


def create_application(db: Session, data: ApplicationCreate):
    obj = Application(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_applications(db: Session, status: StatusEnum | None = None, sort_by: str = "date_applied"):
    query = db.query(Application)
    if status:
        query = query.filter(Application.status == status)
    if sort_by == "date_applied":
        query = query.order_by(Application.date_applied.desc())
    elif sort_by == "company":
        query = query.order_by(Application.company.asc())
    return query.all()


def get_application(db: Session, application_id: int):
    return db.query(Application).filter(Application.id == application_id).first()


def update_application(db: Session, application_id: int, data: ApplicationUpdate):
    obj = get_application(db, application_id)
    if not obj:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj


def delete_application(db: Session, application_id: int):
    obj = get_application(db, application_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


def get_status_summary(db: Session):
    results = (
        db.query(Application.status, func.count(Application.id))
        .group_by(Application.status)
        .all()
    )
    return {status.value: count for status, count in results}

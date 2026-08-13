from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.models import StatusEnum

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=schemas.ApplicationOut, status_code=201)
def create_application(data: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_application(db, data)


@router.get("", response_model=List[schemas.ApplicationOut])
def list_applications(
    status: Optional[StatusEnum] = None,
    sort_by: str = "date_applied",
    db: Session = Depends(get_db),
):
    return crud.get_applications(db, status=status, sort_by=sort_by)


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    return crud.get_status_summary(db)


@router.get("/{application_id}", response_model=schemas.ApplicationOut)
def get_application(application_id: int, db: Session = Depends(get_db)):
    obj = crud.get_application(db, application_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return obj


@router.patch("/{application_id}", response_model=schemas.ApplicationOut)
def update_application(application_id: int, data: schemas.ApplicationUpdate, db: Session = Depends(get_db)):
    obj = crud.update_application(db, application_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return obj


@router.delete("/{application_id}", status_code=204)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_application(db, application_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Application not found")

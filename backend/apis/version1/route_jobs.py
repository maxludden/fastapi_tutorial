from db.repository.jobs import create_new_job
from db.repository.jobs import retrieve_job
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.jobs import JobCreate
from schemas.jobs import ShowJob
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):  # type: ignore
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)  # type: ignore
    return job


# new function
@router.get(
    "/get/{id}", response_model=ShowJob
)  # if we keep just "{id}" . it would stat catching all routes
def read_job(id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)  # type: ignore
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with this id {id} does not exist",
        )
    return job

from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session
from app import schemas, db, background, error_handlers
from fastapi import HTTPException
from typing import List

def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

router = APIRouter(prefix="/feedback", tags=["feedback"])

@router.post("/", response_model=schemas.FeedbackRead, status_code=status.HTTP_201_CREATED)
def create_feedback(feedback: schemas.FeedbackCreate, background_tasks: BackgroundTasks, db_session: Session = Depends(get_db)):
    feedback_obj = db.Feedback(**feedback.dict())
    db_session.add(feedback_obj)
    db_session.commit()
    db_session.refresh(feedback_obj)
    background_tasks.add_task(background.send_thank_you_email, feedback_obj.name, feedback_obj.email, feedback_obj.product)
    return feedback_obj

@router.get("/", response_model=List[schemas.FeedbackRead])
def get_all_feedback(db_session: Session = Depends(get_db)):
    feedbacks = db_session.query(db.Feedback).all()
    return feedbacks

@router.get("/{feedback_id}", response_model=schemas.FeedbackRead)
def get_feedback_by_id(feedback_id: int, db_session: Session = Depends(get_db)):
    feedback_obj = db_session.query(db.Feedback).filter_by(id=feedback_id).first()
    if not feedback_obj:
        raise error_handlers.FeedbackNotFound(feedback_id)
    return feedback_obj

@router.delete("/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feedback(feedback_id: int, db_session: Session = Depends(get_db)):
    feedback_obj = db_session.query(db.Feedback).filter_by(id=feedback_id).first()
    if not feedback_obj:
        raise error_handlers.FeedbackNotFound(feedback_id)
    db_session.delete(feedback_obj)
    db_session.commit()
    return

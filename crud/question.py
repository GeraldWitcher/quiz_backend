from fastapi import Request
from sqlalchemy.orm import Session
from sqlalchemy import desc
import models as mod


async def read_question(exam_id, subject_id, db: Session):
    result = db.query(mod.Question)
    if exam_id:
        result = result.filter(mod.Question.exam_id == exam_id)
    if subject_id:
        result = result.filter(mod.Question.subject_id == subject_id)        
    result = result.order_by(desc(mod.Question.id)).all()
    return result

async def create_question(req: mod.questionSchema, db: Session):
    new_add = mod.Question(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


async def delete_question(id, db: Session):
    new_delete = db.query(mod.Question)\
        .filter(mod.Question.id == id)\
            .delete(synchronize_session=False)
    db.commit()
    return True
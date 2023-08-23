from fastapi import Request
from sqlalchemy.orm import Session
from sqlalchemy import desc
import models as mod


async def read_exam(db: Session):
    return db.query(mod.Exam).order_by(desc(mod.Exam.id)).all()



async def create_exam(req: mod.examSchema, db: Session):
    new_add = mod.Exam(
        name = req.name,
        description = req.description,
        time = req.time,
        status = req.status
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


async def update_status(id, req: mod.examStatusSchema, db: Session):
    new_update = db.query(mod.Exam).filter(mod.Exam.id == id)\
        .update({
            mod.Exam.status: req.status
        }, synchronize_session=False)
    db.commit()
    return new_update


async def delete_exam(id: int, db: Session):
    new_delete = db.query(mod.Exam)\
        .filter(mod.Exam.id == id)\
            .delete(synchronize_session=False)
    db.commit()
    return True


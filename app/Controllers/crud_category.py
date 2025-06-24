from sqlalchemy.orm import Session
from app import models, schemas



def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_category(db:Session,category_id:int):
    return db.query(models.Category).filter(models.Category.cid == category_id).first()
def get_all_category(db:Session):
    return db.query(models.Category).all()


def update_category(db: Session, category_id: int, updates: schemas.CategoryUpdate):
    category = db.query(models.Category).filter(models.Category.CID == category_id).first()
    if category:
        for key, value in updates.model_dump(exclude_unset=True).items():
            setattr(category, key, value)
        db.commit()
        db.refresh(category)
    return category



def delete_category(db: Session, category_id: int):
    category = db.query(models.Category).get(category_id)
    if category:
        db.delete(category)
        db.commit()
    return category
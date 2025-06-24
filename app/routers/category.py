from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import get_db
from app.schemas import CategoryCreate, CategoryUpdate  # ✅ Pydantic schemas
from app.models import Category  # ✅ SQLAlchemy model
from typing import List



router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[schemas.Category])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return [schemas.Category.model_validate(cat) for cat in categories]

@router.get("/{category_id}", response_model=schemas.Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.CID == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# Create category
@router.post("/", response_model=dict)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.CNAME == category.cname).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category name already exists.")
    new_category = Category(CNAME=category.cname, DESCRIPTION=category.description)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"message": "Category created", "id": new_category.CID}


# Update category
@router.put("/{category_id}", response_model=dict)
def update_category(category_id: int, updated_data: CategoryUpdate, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.CID == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(category, key, value)
    db.commit()
    return {"message": "Category updated"}

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.CID == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"message": "Category deleted"}

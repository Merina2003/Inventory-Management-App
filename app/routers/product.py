from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import get_db
from app.schemas import ProductCreate, ProductUpdate  # Pydantic schemas
from app.models import Product  # SQLAlchemy model

router = APIRouter(prefix="/products", tags=["products"])


# Get all products
@router.get("/", response_model=List[schemas.Product])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return [schemas.Product.model_validate(p) for p in products]


# Get product by ID
@router.get("/{product_id}", response_model=schemas.Product)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.PID == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Create product
@router.post("/", response_model=dict)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    existing = db.query(Product).filter(Product.PNAME == product.pname).first()
    if existing:
        raise HTTPException(status_code=400, detail="Product name already exists.")

    new_product = Product(
        PNAME=product.pname,
        PRICES=product.prices,
        STOCK=product.stock,
        MIN_QUANTITY=product.min_quantity,
        CID=product.cid
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product created", "id": new_product.PID}


# Update product
@router.put("/{product_id}", response_model=dict)
def update_product(product_id: int, updated_data: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.PID == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    return {"message": "Product updated"}


# Delete product
@router.delete("/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.PID == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}
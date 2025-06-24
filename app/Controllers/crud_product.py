from sqlalchemy.orm import Session
from app import models, schemas


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        PNAME=product.pname,
        PRICES=product.prices,
        STOCK=product.stock,
        MIN_QUANTITY=product.min_quantity,
        CID=product.cid
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.pid == product_id).first()

def get_all_product(db:Session):
    return db.query(models.Product).all()

# Update an existing product
def update_product(db: Session, product_id: int, updated_product: schemas.ProductUpdate):
    product = db.query(models.Product).filter(models.Product.PID == product_id).first()
    if product:
        product.PNAME = updated_product.pname
        product.CID = updated_product.cid
        product.STOCK = updated_product.stock
        product.MIN_QUANTITY = updated_product.min_quantity
        product.PRICES = updated_product.prices
        db.commit()
        db.refresh(product)
    return product

# Delete a product
def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).get(product_id)
    if product:
        db.delete(product)
        db.commit()
    return product

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum, DECIMAL, DateTime, Computed
from sqlalchemy.orm import relationship
from app.database import Base

from enum import Enum as PyEnum

class TransactionTypeEnum(PyEnum):
    PURCHASE = "PURCHASE"
    SALE = "SALE"

class Category(Base):
    __tablename__ = "CATEGORYS"

    CID = Column(Integer, primary_key=True, autoincrement=True)
    CNAME = Column(String(100), nullable=False, unique=True)
    DESCRIPTION = Column(String(255))

    # FIX: Use model class name "Product"
    PRODUCTS = relationship("Product", back_populates="CATEGORY")

class Product(Base):
    __tablename__ = "PRODUCTS"

    PID = Column(Integer, primary_key=True, autoincrement=True)
    PNAME = Column(String(100), nullable=False)
    CID = Column(Integer, ForeignKey("CATEGORYS.CID"), nullable=False)
    STOCK = Column(Integer, default=0)
    MIN_QUANTITY = Column(Integer, default=5)
    PRICES = Column(Float, nullable=False)

    # FIX: use model class names in relationship()
    CATEGORY = relationship("Category", back_populates="PRODUCTS")
   # PURCHASES = relationship("Purchase", back_populates="PRODUCT")
    # SALES = relationship("Sale", back_populates="PRODUCT")
    TRANSACTION_S = relationship("Transaction", back_populates="PRODUCT")

class Transaction(Base):
    __tablename__ = "TRANSACTION_S"

    TRANSACTION_ID = Column(Integer, primary_key=True, autoincrement=True)
    PID = Column(Integer, ForeignKey("PRODUCTS.PID"), nullable=False)
    TRANSACTION_TYPE = Column(Enum(TransactionTypeEnum), nullable=True)
    QUANTITY = Column(Integer, nullable=False)
    UNIT_PRICE = Column(Float, nullable=True)
    WHOLE_PRICE = Column(DECIMAL(10, 2), Computed("UNIT_PRICE * QUANTITY", persisted=True))
    TIMESTAMP = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    PRODUCT = relationship("Product", back_populates="TRANSACTION_S")




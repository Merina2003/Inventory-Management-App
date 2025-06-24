from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    cname: str = Field(alias="CNAME")
    description: Optional[str] = Field(default=None, alias="DESCRIPTION")

    model_config = {
        "populate_by_name": True,  # Allows using 'cname' and 'description' from JSON
    }

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    cname: Optional[str] = Field(default=None, alias="CNAME")
    description: Optional[str] = Field(default=None, alias="DESCRIPTION")

    model_config = {
        "populate_by_name": True
    }

class Category(CategoryBase):
    cid: int = Field(alias="CID")

    model_config = {
        "from_attributes": True,
        "populate_by_name": True
    }


class ProductBase(BaseModel):
    pname: str = Field(alias="PNAME")
    prices: float = Field(alias="PRICES")
    stock: Optional[int] = Field(default=0, alias="STOCK")
    min_quantity: Optional[int] = Field(default=5, alias="MIN_QUANTITY")
    cid: int = Field(alias="CID")

    model_config = {
        "populate_by_name": True
    }

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    pname: Optional[str] = Field(default=None, alias="PNAME")
    prices: Optional[float] = Field(default=None, alias="PRICES")
    stock: Optional[int] = Field(default=None, alias="STOCK")
    min_quantity: Optional[int] = Field(default=None, alias="MIN_QUANTITY")
    cid: Optional[int] = Field(default=None, alias="CID")

    model_config = {
        "populate_by_name": True
    }

class Product(ProductBase):
    pid: int = Field(alias="PID")

    model_config = {
        "from_attributes": True,
        "populate_by_name": True
    }

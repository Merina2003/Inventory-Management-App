from fastapi import FastAPI
from app.database import engine, Base
from app.routers import product, category

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product.router)
app.include_router(category.router)
@app.get("/")
def root():
    return {"message": "Inventory System Running!"}



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
load_dotenv()
DB_USER=os.getenv('DB_USERNAME')
DB_PASSWORD= quote_plus(os.getenv('DB_PASSWORD'))
DB_HOST=os.getenv('DB_HOST')
DB_NAME=os.getenv('DB_DATABASE')
DB_PORT=os.getenv('DB_PORT')

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
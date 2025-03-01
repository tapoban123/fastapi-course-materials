from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
DATABASE_NAME = os.environ["DATABASE"]

URL_DATABASE = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DATABASE_NAME}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

Base = declarative_base()
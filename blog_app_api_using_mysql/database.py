from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")


URL_DATABASE = f"mysql+pymysql://{USER_NAME}:{PASSWORD}@localhost:3306/blogapplication"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

Base = declarative_base()

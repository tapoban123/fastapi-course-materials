import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Neon Postgresql has been used here.
DB_URL = os.environ.get("POSTGRES_DB_URL")

DATABASE_URL = f"postgresql+asyncpg{DB_URL}"

engine = create_async_engine(DATABASE_URL)

Base = declarative_base()

async_session = sessionmaker(
    class_=AsyncSession,
    expire_on_commit=False,
    bind=engine,
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
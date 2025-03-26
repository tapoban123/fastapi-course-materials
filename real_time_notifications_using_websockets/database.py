from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = ""

engine = create_async_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(
    class_=AsyncSession,
    expire_on_commit=False,
    bind=engine,
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
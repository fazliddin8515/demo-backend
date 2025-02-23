import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DB_URI = os.getenv("DB_URI", "")

engine = create_async_engine(DB_URI)

AsyncSession = async_sessionmaker(engine)

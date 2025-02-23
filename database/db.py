from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    "postgresql+asyncpg://postgres:root_123@localhost:5432/demo"
)

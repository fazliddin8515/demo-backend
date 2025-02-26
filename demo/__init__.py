import os

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select

from database.db import AsyncSession
from database.models import User

app = FastAPI()


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


@app.get("/api", response_model=dict[str, list[UserResponse]])
async def get_users() -> dict[str, list[UserResponse]]:
    async with AsyncSession() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()

        return {"users": [UserResponse.model_validate(user) for user in users]}

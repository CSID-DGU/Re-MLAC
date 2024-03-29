from pydantic import BaseModel, Field
from typing import Optional


class BodySchema(BaseModel):
    timestamp: str = Field(None, alias="timestamp")
    username: Optional[str] = Field(None, alias="username")
    password: Optional[str] = Field(None, alias="password")
    script: Optional[str] = Field(None, alias="script")

    class Config:
        exclude_none = True

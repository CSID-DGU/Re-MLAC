from app.configs.database import Base
from app.types.e_attack import EAttack
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import ENUM


class DummyScriptModel(Base):
    __tablename__: str = "dummy_scripts"
    id: int = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    content: str = Column("content", String)
    attack_type: str = Column("type", ENUM(EAttack))

from app.configs.database import Base
from app.types.e_attack import EAttack
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import ENUM


class DummyUserModel(Base):
    __tablename__: str = "dummy_users"
    id: int = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    username: str = Column("username", String)
    password: str = Column("password", String)
    attack_type: str = Column("type", ENUM(EAttack))

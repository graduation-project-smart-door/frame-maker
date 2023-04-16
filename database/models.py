from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
metadata = BaseModel.metadata


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    label = Column(Text, nullable=False)

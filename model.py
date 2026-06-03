from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float

class Base(DeclarativeBase):
    pass

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    note = Column(String)
    date_posted = Column(String)
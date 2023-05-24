from typing import List
from typing import Optional
from sqlalchemy import Column, ForeignKey, Integer, create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy import create_engine

db_path = "/home/teddy/Documents/StockScreener/app/database/database_file.db"
engine = create_engine("sqlite:///" + db_path)

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class Stock(Base):
    __tablename__ = "stock"
    id =Column(Integer, primary_key = True)
    ticker= Column(String)
    company = Column(String)
    stock_detail = relationship("StockDetail", back_populates= 'stock')

class stockDetail(Base):
    __tablename__ = "stock_details"
    stock_id= Column(Integer, ForeignKey("stock.id"), primary_key= True)
    stock = relationship("Stock", back_populates= 'stock_details')

Base.metadata.create_all(engine)
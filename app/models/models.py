from sqlalchemy import Column, Integer, MetaData, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database.database import Base

class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True, autoincrement= True, unique=True)
    ticker = Column(String)
    company = Column(String)
    industry = Column(String, nullable= True)
    marketCap = Column(Float, nullable= True)
    recommendationMean = Column(Float, nullable= True)
    forwardPE = Column(Float, nullable= True)
    high = Column(Float, nullable= True)
    low = Column(Float, nullable= True)
    volume  = Column(Float, nullable= True)
    currentPrice = Column(Float, nullable= True)
    fiftyTwoWeekLow = Column(Float, nullable= True)
    fiftyTwoWeekHigh = Column(Float, nullable= True)

    stock_detail = relationship("StockDetail", back_populates="stock")

class StockDetail(Base):
    __tablename__ = "stock_details"
   
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key=True)  # This column is part of the composite primary key
    date = Column(String, primary_key=True)
    
    close = Column(Float)
    volume  = Column(Float)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    target_price = Column(Float)
    forward_pe = Column(Float)
    p_e = Column(Float)
    dividend = Column(Float)
    earnings = Column(Float)

    

    stock = relationship("Stock", back_populates="stock_detail")



from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
from app.database.database import SessionLocal
from app.models.models import Stock, Token, User, UserOut,UserIn
from app.services.home import  add_stock_ticker, fetch_tickers, fetch_tickers_api, filtered_tickers, get_db, load_tickers_from_file, populate_stock_table
from app.services.stocks import fetch_stock_db, fetch_stock_history, populate_stock_detail_table
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import time
from app.services.user import UserManager
from app.utils.Authentificate import Authentificate 


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.post("/initialise-database")
async def initialize_database(db:Session() =Depends(get_db)): # type: ignore
    #fetch filtered, valid tickers
    
    valid_tickers = load_tickers_from_file("app/database/tickers.json")
    add_stock_ticker(valid_tickers, db)
    #populate table stock
    populate_stock_table(db)
    start = time.time()
    populate_stock_detail_table(db)


    return{"stocks": "populated"}
@router.post("/home/history/{symbol}")
async def home(symbol: str, background_tasks: BackgroundTasks, db:Session() =Depends(get_db)):   # type: ignore
    stockHistory =  fetch_stock_history(symbol, db)
    return {"status":stockHistory}

@router.get("/home/")
async def root( db = Depends(get_db)):
    pass


@router.get("/home/{symbol}")
async def root(symbol: str, db = Depends(get_db)):
    stock = fetch_stock_db(symbol, db)
    return { "stocks": stock}
@router.get("/home/history/{symbol}")
async def get_stock_history(symbol: str, db = Depends(get_db)):
    stock_history = fetch_stock_history(symbol, db)
    return stock_history




@router.post("/users/", response_model = UserOut)
async def create_user(user:UserIn, db: Session = Depends(get_db)) -> any:
    new_user = UserManager.create_user(user, db)
    return { "new_user": new_user}

@router.post("/token")
async def login_for_access_token(form_data,
                                db:Session= Depends(get_db)) -> Token:
    user = Authentificate.authenticate_user(form_data["username"], form_data["password"], db )
    if not user:
        raise HTTPException( 
            
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "incorrect credentials",
        )
   
    token_expiration_time =  Authentificate.token_expiration()
    access_token = Authentificate.create_jwt_token( data ={ "sub": user.username}, expires_delta = token_expiration_time)
    
    return access_token


@router.get("/items")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)] ):
    return {"token":token}
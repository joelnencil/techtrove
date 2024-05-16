import fastapi
from fastapi import FastAPI, APIRouter, Depends, Request,status,Form
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from models import UserDetails
from pydantic import BaseModel
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import UserDetails, Base


# PostgreSQL database connection Configuration

app = FastAPI()
router = APIRouter()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    email: str
    password: str

@app.get('/',response_class=HTMLResponse,include_in_schema=False)
def form(request:Request):
    return templates.TemplateResponse("/index.html",{"request":request})

    
    
@app.get("/account",response_class=HTMLResponse)
def dashboard(request:Request):
    print("hello world")
    return templates.TemplateResponse("/account.html",{"request":request})

@app.get("/products",response_class=HTMLResponse)
def dashboard(request:Request):
    print("hello world")
    return templates.TemplateResponse("/products.html",{"request":request})





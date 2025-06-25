from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", tags=["general"])
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/pago", tags=["general"])
def index(request: Request):
    return templates.TemplateResponse("pago_integrado_simple.html", {"request": request})

@router.get("/conocenos", tags=["general"])
def conocenos(request: Request):
    return templates.TemplateResponse("conocenos.html", {"request": request})

@router.get("/historico", tags=["general"])
def historico(request: Request):
    return templates.TemplateResponse("historico.html", {"request": request})

@router.get("/faq", tags=["general"])
def faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})
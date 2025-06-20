from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.schemas import PagoCreate
from app.database import SessionLocal
from app.models import Pago

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def form_pago(request: Request):
    return templates.TemplateResponse("pago_form.html", {"request": request})

@router.post("/guardar")
def guardar_pago(
    request: Request,
    usuario_email: str = Form(...),
    monto: float = Form(...),
    moneda: str = Form(...),
    metodo_pago: str = Form(...),
    estado: str = Form(...),
    referencia_externa: str = Form(...)
):
    data = PagoCreate(
        usuario_email=usuario_email,
        monto=monto,
        moneda=moneda,
        metodo_pago=metodo_pago,
        estado=estado,
        referencia_externa=referencia_externa
    )

    db = SessionLocal()
    try:
        nuevo_pago = Pago(**data.dict())
        db.add(nuevo_pago)
        db.commit()
        db.refresh(nuevo_pago)
    except Exception as e:
        db.rollback()
    finally:
        db.close()

    return RedirectResponse("/", status_code=303)

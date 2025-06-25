from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/pago", tags=["pagos"])
def formulario_pago(request: Request):
    return templates.TemplateResponse("pago_integrado_simple.html", {"request": request})

@router.post("/guardar", tags=["pagos"])
def guardar_pago(
    request: Request,
    nombre_completo: str = Form(...),
    usuario_email: str = Form(...),
    usuario_melee: str = Form(...),
    codigo_postal: str = Form(...)
):
    print("Pago recibido:", nombre_completo, usuario_email, usuario_melee, codigo_postal)
    return RedirectResponse("/pago", status_code=303)

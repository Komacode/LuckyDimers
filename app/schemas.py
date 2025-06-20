from pydantic import BaseModel, EmailStr, Field

class PagoCreate(BaseModel):
    usuario_email: EmailStr
    monto: float = Field(gt=0)
    moneda: str
    metodo_pago: str
    estado: str
    referencia_externa: str

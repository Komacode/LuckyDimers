from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_email = Column(String, index=True, nullable=False)
    monto = Column(Float, nullable=False)
    moneda = Column(String, nullable=False)
    metodo_pago = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    referencia_externa = Column(String, unique=True, nullable=False)
    fecha_hora = Column(DateTime, default=datetime.utcnow)

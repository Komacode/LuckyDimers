from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import pagos

app = FastAPI()
app.include_router(pagos.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

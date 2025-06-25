from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import pagos, general

app = FastAPI()

app.include_router(pagos.router)
app.include_router(general.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

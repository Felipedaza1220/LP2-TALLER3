from fastapi import FastAPI

from .database import Base, engine
from .routers import categorias, productos


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Tienda Virtual API",
    description="API REST de la Tienda Virtual",
    version="1.0.0"
)


app.include_router(productos.router)
app.include_router(categorias.router)

import json
import os

from .database import SessionLocal
from .models import Categoria, Producto


RUTA_PRODUCTOS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "productos.json"
)


def cargar_datos():
    with open(RUTA_PRODUCTOS, encoding="utf-8") as archivo:
        datos = json.load(archivo)

    db = SessionLocal()
    productos_cargados = 0

    try:
        for item in datos:
            categoria = (
                db.query(Categoria)
                .filter(Categoria.nombre == item["categoria"])
                .first()
            )

            if categoria is None:
                categoria = Categoria(
                    nombre=item["categoria"]
                )
                db.add(categoria)
                db.flush()

            producto_existente = (
                db.query(Producto)
                .filter(Producto.sku == item["sku"])
                .first()
            )

            if producto_existente:
                continue

            producto = Producto(
                sku=item["sku"],
                marca=item["marca"],
                nombre=item["nombre"],
                precio=item["precio"],
                foto=item["foto"],
                stock=item["stock"],
                activo=item["activo"],
                categoria_id=categoria.id
            )

            db.add(producto)
            productos_cargados += 1

        db.commit()

        print(
            f"Se cargaron {productos_cargados} productos correctamente."
        )

    finally:
        db.close()


if __name__ == "__main__":
    cargar_datos()

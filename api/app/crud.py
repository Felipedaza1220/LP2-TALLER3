from sqlalchemy.orm import Session

from . import models


def obtener_productos(
    db: Session,
    categoria_id: int | None = None
):
    consulta = db.query(models.Producto)

    if categoria_id is not None:
        consulta = consulta.filter(
            models.Producto.categoria_id == categoria_id
        )

    return consulta.all()


def obtener_producto(db: Session, sku: str):
    return (
        db.query(models.Producto)
        .filter(models.Producto.sku == sku)
        .first()
    )


def obtener_categorias(db: Session):
    return db.query(models.Categoria).order_by(
        models.Categoria.nombre
    ).all()

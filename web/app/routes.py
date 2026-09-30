from flask import Blueprint, render_template, request

from . import api_client


bp = Blueprint("main", __name__)


@bp.route("/")
def inicio():
    categoria_id = request.args.get(
        "categoria_id",
        type=int
    )

    productos = api_client.obtener_productos(
        categoria_id=categoria_id
    )

    categorias = api_client.obtener_categorias()

    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_id=categoria_id
    )


@bp.route("/producto/<sku>")
def detalle(sku):
    producto = api_client.obtener_producto(sku)

    if producto is None:
        return render_template(
            "detalle.html",
            producto=None
        ), 404

    return render_template(
        "detalle.html",
        producto=producto
    )


@bp.route("/categorias")
def categorias():
    categorias = api_client.obtener_categorias()

    return render_template(
        "categorias.html",
        categorias=categorias
    )

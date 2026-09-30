import os


SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "clave-secreta-desarrollo"
)

API_URL = os.environ.get(
    "API_URL",
    "http://localhost:8000"
)

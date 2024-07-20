from pydantic import BaseModel

from typing import Optional


class Products (BaseModel):
    id : Optional[int | None] = None
    nombre : str
    precio_compra : float
    precio_venta : float
    provedor : Optional[str | None] = None

products = []
from enum import Enum

from pydantic import BaseModel

from typing import Optional



class Products (BaseModel):
    id : Optional[int | None] = None
    nombre : str
    precio_compra : float
    precio_venta : float
    provedor : Optional[str | None] = None

class ModelName (str ,Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


products = []

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


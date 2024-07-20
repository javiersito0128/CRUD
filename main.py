from fastapi import FastAPI
from uuid import uuid4 as id4

from models.api_products import products, Products


app = FastAPI()


@app.get("/")
def read_root():
    return {'Hi mother fuckers'}

@app.get ('/products')
def obtein_products ():
    return products

@app.post ('/products')
def create_products (product : Products):
    product.id = str(id4())
    products.append(product)
    return {f'The product has been created'}

@app.get('/product/{product_id}')
def obtain_product_by_id (product_id : str):
    result = filter(lambda product : product.id == product_id, products)
    
    for product in result:
        return product
    
    return {f"The product {product_id} doesn't exist"}


from fastapi import FastAPI

from models.api_products import products, Products

app = FastAPI()


@app.get("/")
def read_root():
    return {'Hi mother fuckers'}

@app.get('/products')
def obtein_products ():
    return products

@app.post('/products')
def create_products (product : Products):
    products.append(product)
    return {f'The product has been created'}


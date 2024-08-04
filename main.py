from fastapi import FastAPI, HTTPException
from uuid import uuid4 as id4

from models.clases import products, Products, ModelName


app = FastAPI()


@app.get ("/")
def read_root():
    return {'Hi mother fuckers'}


@app.get ('/products')
def obtein_products ():
    return products


@app.get ('/product/{product_id}')
def obtain_product_by_id (product_id : str):
    result = filter(lambda product : product.id == product_id, products)
    
    for product in result:
        return product
    
    raise HTTPException(status_code = 404, detail = f"The product {product_id} doesn't exist")


@app.post ('/products')
def create_products (product : Products):
    product.id = str(id4())
    products.append(product)
    return {f'The product has been created'}


@app.put ('/product/{product_id}')
def update_product_by_id(product_id : str, product_new : Products):
    result = filter(lambda product : product.id == product_id, products)
    
    for product in result:
        product.nombre = product_new.nombre
        product.precio_compra = product_new.precio_compra
        product.precio_venta = product_new.precio_venta
        product.provedor = product_new.provedor
        return f'The product {product_id} has been updated'
    
    raise HTTPException(status_code = 404, detail = f"The product {product_id} doesn't exist")


@app.delete ('/product/{product_id}')
def delete_product_by_id(product_id : str):
    result = filter(lambda product : product.id == product_id, products)
    
    for product in result:
        products.remove(product)
        return f'The product {product_id} has been deleted'
    
    raise HTTPException(status_code = 404, detail = f"The product {product_id} doesn't exist")

@app.get('/models/{modelsname}')
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name' : model_name, 'message' : 'Deep learing FTW!'}

    if model_name.value == 'lenet':
        return {'model_name' : model_name, 'message' : 'LeCNN all the images'}
    
    
    return {'model_name' : model_name, 'message' : 'Have some residuals'}


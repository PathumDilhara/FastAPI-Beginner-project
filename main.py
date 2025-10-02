from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello fast api"



products = [
    Product(id=1, name="Phone", description="budget phone", price=200, quantity=6),
    Product(id=2, name="laptop", description="budget laptop", price=300, quantity=60),
    Product(id=3, name="tab", description="budget tab", price=400, quantity=60),
    Product(id=4, name="data-cable", description="budget data-cable", price=500, quantity=40),
    Product(id=5, name="pc", description="budget pc", price=600, quantity=456),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{id}")
def get_product_by_id(id: int):
    return products[id]


@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products")
def update_products(id: int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = [product]
            return "Product updating success"
    return "No product found"
        
@app.delete("/products")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted success"
    return "No product found"

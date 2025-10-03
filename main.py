from fastapi import FastAPI, Depends
from models import Product
from database_config import session, engine

import database_models

from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind= engine)



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


# Dependency injection
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()



def init_db():
    db = session()

    count = db.query(database_models.Product).count
    if count==0:
        for item in products:
            db.add(database_models.Product(**item.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)): # Dependency injection
    # Databse connection
    # db = session()
    # db.query()

    db_products = db.query(database_models.Product).all()   
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_product:
        return db_product
    return "Product not founds"


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    # products.append(product)

    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products")
def update_products(id: int, product:Product, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = [product]
    #         return "Product updating success"
    db_product  = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Db product updated"
    return "No product found"
        
@app.delete("/products")
def delete_product(id:int, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         del products[i]
    #         return "Product deleted success"

    db_product  = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_product:
        db.delete(db_product)
        db.commit() 
        return "Product deleted"
    else:
        return "No product found"

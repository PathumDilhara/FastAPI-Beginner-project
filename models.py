from pydantic import BaseModel

# No need constructir, but models fields should be defined

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int   

#  Since we use pydentic these no need constructor or validation

# class Product:
#     id: int
#     name: str
#     description: str
#     price: float
#     quantity: int

#     # SInce we use pydentic these no need
#     # Constructor
#     def __init__(self, id: int, name: str, description: str, price: float,  quantity: int):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity = quantity
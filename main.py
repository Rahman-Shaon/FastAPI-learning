from fastapi import FastAPI
from mockData import products

app = FastAPI()


@app.get("/")           # eta diye bujhte parbe kon page load korte hobe / diye home page bojhano hoi
def home():
    return "Welcome"

@app.get("/login")
def loginpage():
    return "Successfully login"


## all products

@app.get("/products")
def get_products():
    return products



## Finding exact product with the id number
## Path Params..

@app.get("/product/{product_id}")
def productlist(product_id:int):

    for product in products:
        if product.get("id") == product_id:
            return product

    return{
        "error": "Product not fuound"
    }




@app.get("/greet")
def greet_user(name:str, age:int):
    return{
        "greet": f"Hello {name}, Your age is {age}"
    }
from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

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




# @app.get("/greet")
# def greet_user(name:str, age:int):
#     return{
#         "greet": f"Hello {name}, Your age is {age}"
#     }



@app.get("/greet")
def greet_user(request:Request):
    query_params = request.query_params

    return{
        "greet": f"Hello {query_params.get("name")}, Your age is{query_params.get("age")}"
    }


# data ki ki vabe pathano jai? -->> body, headers - request headers, query params



## differnt type of HTTP methods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    # print(product_data)
    product_data = product_data.model_dump()
    # print(product_data)
    products.append(product_data)

    return {"status":"Product Created Successfully...", "data":products}




@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):

    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data
            return {"status":"Product Updated Successfully..", "Product":product_data}

    return {"error":"Product not found fo rthis id"}



@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status":"Product deleted successfully..", "product":delete_product}

    return {"error":"Product not found fo rthis id"}






## pydentic


## Postman
# How to call different HTTP Methods. - Any tool?

# how to dalidate data -- DTOS
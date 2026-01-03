from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI E-commerce Application!"}

@app.get("/products/{id}")
def read_product(id: int):
    products = ["Laptop", "Smartphone", "Tablet", "Headphones"]
    return products[id] if 0 <= id < len(products) else {"error": "Product not found"}
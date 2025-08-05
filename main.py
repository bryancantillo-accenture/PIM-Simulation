from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

inventory = [
    { "Product": "Microwave", "SKU": "MW837291" },
    { "Product": "Microwave", "SKU": "MW102938" },
    { "Product": "Microwave", "SKU": "MW564738" },
    { "Product": "Refrigerator", "SKU": "RF384729" },
    { "Product": "Refrigerator", "SKU": "RF927384" },
    { "Product": "Refrigerator", "SKU": "RF102983" },
    { "Product": "Washing Machine", "SKU": "WM837492" },
    { "Product": "Washing Machine", "SKU": "WM293847" },
    { "Product": "Washing Machine", "SKU": "WM928374" },
    { "Product": "Dryer", "SKU": "DR102938" },
    { "Product": "Dryer", "SKU": "DR837465" },
    { "Product": "Dryer", "SKU": "DR564738" },
    { "Product": "Dishwasher", "SKU": "DW837192" },
    { "Product": "Dishwasher", "SKU": "DW182736" },
    { "Product": "Dishwasher", "SKU": "DW918273" }
]


inventory.count = len(inventory)


@app.get("/products")
def get_products():
    """Retrieve the list of products in the inventory."""
    return JSONResponse(content=inventory, count=inventory.count, status_code=200)

@app.post("/product")
def add_product(product: dict):
    """Add a new product to the inventory."""
    'Test'
    inventory.append(product)   
    return JSONResponse(content={"message": "Product added successfully", "product": product}, status_code=201)
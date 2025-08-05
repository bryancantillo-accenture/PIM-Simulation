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


@app.get("/")
def read_root():
    """Root endpoint to check if the API is running."""
    return JSONResponse(content={"message": "Welcome to the PIM Simulation API"}, status_code=200)

@app.get("/products")
def get_products():
    """Retrieve the list of products in the inventory."""
    contentResult = {
        "message": "List of products in the inventory",
        "count": len(inventory),
        "products": inventory
    }
    return JSONResponse(content=contentResult, status_code=200)

@app.post("/product")
def add_product(product: dict):
    """Add a new product to the inventory."""
    'Test'
    inventory.append(product)   
    return JSONResponse(content={"message": "Product added successfully", "product": product}, status_code=201)
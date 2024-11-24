from fastapi import APIRouter, status

inventory_router = APIRouter(
    prefix="/inventory"
)

@inventory_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_inventor():
    pass

@inventory_router.post("/add-products", status_code=status.HTTP_201_CREATED)
async def add_products():
    pass

@inventory_router.get("/{productid}")
async def get_product(productid: str):
    pass

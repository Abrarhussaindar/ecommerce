from fastapi import APIRouter, status

product_router = APIRouter(
    prefix="/product"
)

@product_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_product():
    pass

@product_router.get("/{uid}", status_code=status.HTTP_200_OK)
async def get_product(uid: str):
    pass

@product_router.get("/all")
async def get_all_products():
    return []

@product_router.get("/category/{cate}", status_code=status.HTTP_200_OK)
async def get_product_by_category(cate: str):
    pass

@product_router.put("/update/{uid}", status_code=status.HTTP_200_OK)
async def update_product(uid: str):
    pass

@product_router.delete("/{uid}", status_code=status.HTTP_200_OK)
async def delete_product(uid: str):
    pass


from fastapi import APIRouter, status

cart_router = APIRouter(
    prefix="/cart"
)

@cart_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_new_cart():
    pass


@cart_router.get("/{cartid}")
async def get_cart(cartid: str):
    pass


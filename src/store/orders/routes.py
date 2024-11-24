from fastapi import APIRouter, status

order_router = APIRouter(
    prefix="/order"
)

@order_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_new_order():
    pass

@order_router.get("/{orderid}", status_code=status.HTTP_200_OK)
async def get_order_by_id(orderid: str):
    pass

@order_router.get("/{uid}", status_code=status.HTTP_200_OK)
async def get_order_by_userid(uid: str):
    pass

@order_router.put("/update/{orderid}", status_code=status.HTTP_200_OK)
async def update_order(orderid: str):
    pass

@order_router.delete("/delete/{orderid}", status_code=status.HTTP_200_OK)
async def delete_order(orderid: str):
    pass
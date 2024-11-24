from fastapi import  FastAPI
from contextlib import asynccontextmanager
import uvicorn

from src.auth.routes import auth_router
from src.database.db import init_db
from src.store.cart.routes import cart_router
from src.store.inventory.routes import inventory_router
from src.store.orders.routes import order_router
from src.store.products.routes import product_router
from src.users.routes import user_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"server is starting...")
    await init_db()
    yield
    print(f"server has been stopped")

app = FastAPI(
    title="Ecommerce",
    description='An Ecommerce backend service',
    lifespan=life_span
)

app.include_router(user_router, tags=["User"])
app.include_router(auth_router, tags=["Auth"])
app.include_router(product_router, tags=["Product"])
app.include_router(order_router, tags=["Order"])
app.include_router(inventory_router, tags=["Inventory"])
app.include_router(cart_router, tags=['Cart'])

@app.get("/", tags=["root"])
async def root():
    return {"message": "An Ecommerce backend service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.__init__:app", host="127.0.0.1", port=8080, reload=True)

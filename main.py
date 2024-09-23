from fastapi import FastAPI
from routers.orders import router as orders_router

app = FastAPI()

app.include_router(orders_router)
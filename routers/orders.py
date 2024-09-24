from fastapi import APIRouter
from datetime import date
from core.dependencies import OrderServiceDep
from schemas.orders import OrderCreate

router = APIRouter()


@router.get("/orders/{order_date}")
async def get_orders(order_date: date, order_service: OrderServiceDep):
    orders = await order_service.get_orders_by_date(order_date)
    return orders


@router.post("/orders/")
async def create_order(order: OrderCreate, order_service: OrderServiceDep):
    order_data = order.dict()
    new_order = await order_service.create_order(order_data)
    return new_order

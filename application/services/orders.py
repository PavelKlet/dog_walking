from fastapi import HTTPException

from adapters.repositories.orders import OrderRepository
from application.unit_of_work.unit_of_work import UnitOfWork
from datetime import date, time
from typing import List, Dict, Any
from adapters.repositories.models.ordres import Order


class OrderService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.uow.set_repository('order', OrderRepository)

    async def get_orders_by_date(self, date: date) -> List[Order]:
        async with self.uow:
            orders = await self.uow.order.get_orders_by_date(date)
            return orders

    async def create_order(self, order_data: Dict[str, Any]) -> Order:
        async with self.uow:
            if await self.has_conflicting_order(order_data['date'],
                                                order_data['start_time'],
                                                order_data['walker_name']):
                raise HTTPException(
                    status_code=400,
                    detail="Уже есть активная прогулка на это время для данного имени."
                )
            order = await self.uow.order.add_one(order_data)
            await self.uow.commit()
            return order

    async def has_conflicting_order(self, order_date: date, start_time: time,
                                    walker_name: str) -> bool:
        conflicting_order = await self.uow.order.get_order_by_date_and_time_for_walker(
            order_date, start_time, walker_name)
        return conflicting_order is not None


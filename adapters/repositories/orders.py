from datetime import date, time
from typing import Optional, List

from sqlalchemy import select
from typing_extensions import Sequence

from adapters.repositories.base import SQLAlchemyRepository
from adapters.repositories.models.ordres import Order


class OrderRepository(SQLAlchemyRepository):
    model = Order

    async def get_orders_by_date(self, order_date: date) -> Sequence[Order]:
        stmt = select(self.model).where(self.model.date == order_date)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_order_by_date_and_time_for_walker(
            self,
            order_date: date,
            start_time: time,
            walker_name: str
    ) -> Optional[Order]:

        stmt = select(self.model).where(
            self.model.date == order_date,
            self.model.start_time == start_time,
            self.model.walker_name == walker_name
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

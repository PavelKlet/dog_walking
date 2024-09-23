from fastapi import Depends
from typing import Annotated

from application.services.orders import OrderService
from application.unit_of_work.unit_of_work import UnitOfWork
from .database import async_session_maker

OrderServiceDep = Annotated[OrderService, Depends(lambda: OrderService(UnitOfWork(async_session_maker)))]

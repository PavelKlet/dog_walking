from sqlalchemy import Column, Integer, String, Time, Date
from core.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    apartment_number = Column(String, nullable=False)
    pet_name = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    walker_name = Column(String, nullable=False)

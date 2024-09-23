from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from datetime import date, time, datetime
import pytz


class OrderCreate(BaseModel):
    apartment_number: str
    pet_name: str
    breed: str
    date: date
    start_time: time
    walker_name: str

    @field_validator('start_time')
    @classmethod
    def validate_start_time(cls, start_time: time):

        if start_time.minute not in (0, 30):
            raise HTTPException(
                status_code=400,
                detail="Прогулка может начинаться только в начале часа или в половину."
            )
        if start_time.hour < 7 or start_time.hour > 23:
            raise HTTPException(
                status_code=400,
                detail="Прогулка может быть только между 7:00 и 23:00."
            )
        return start_time

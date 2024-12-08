from pydantic import BaseModel

class Sale(BaseModel):
    title: str
    price: float

class DatePeriod(BaseModel):
    start: str
    end: str
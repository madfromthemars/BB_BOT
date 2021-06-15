from pydantic import BaseModel


class User(BaseModel):
    id: int
    telegram_id: int
    first_name: str
    last_name: str
    user_name: str
    phone_number: str
    barber_id: int

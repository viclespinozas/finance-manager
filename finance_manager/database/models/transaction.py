from pydantic import BaseModel
from typing import Optional


class Transaction(BaseModel):
    id: Optional[str] = None
    description: str
    date: str
    amount: str
    user_id: int
    category_id: int

from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    name: str
    last_name: str
    transactions: List[int]

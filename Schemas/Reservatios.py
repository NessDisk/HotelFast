from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Reservations(BaseModel):
        id:  Optional[int] =None
        user: str
        room: int
        dateStar: datetime
        dateEnd: datetime
        customerName: str
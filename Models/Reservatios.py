from pydantic import BaseModel
from datetime import datetime

class Reservations(BaseModel):
        id:   int
        user: str
        room: int
        dateStar: datetime
        dateEnd: datetime
        customerName: str
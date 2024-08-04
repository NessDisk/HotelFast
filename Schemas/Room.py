from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional

class Room(BaseModel):
        id:  Optional[int] =0
        numRoom: int
        type: Literal['simple', 'doble', 'suite']
        priceByNight: float
        enable:bool 
from pydantic import BaseModel, field_validator, validator
from datetime import datetime
from typing import Optional

class Reservations(BaseModel):
        id:  Optional[int] =None
        customerName: str
        startDate: datetime
        endDate: datetime
        roomId: int 

        # verificar que exista
        @validator('endDate')
        def validateDates(cls, v, values):
                if 'startDate' in values and v < values['startDate']:
                        raise ValueError('endDate must be after startDate')
                return v
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, String, Boolean 
from config.database import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    numRoom = Column(String, unique=True, index=True)
    type = Column(String)
    priceByNight = Column(Float)
    isAvaible = Column(Boolean, default=True)

    reservations = relationship("Reservation", back_populates="room")
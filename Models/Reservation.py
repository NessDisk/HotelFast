from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customerName = Column(String)
    startDate = Column(Date)
    endDate = Column(Date)
    roomId = Column(Integer, ForeignKey("rooms.id"))

    room = relationship("Room", back_populates="reservations")
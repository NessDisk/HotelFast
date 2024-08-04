from fastapi import HTTPException
from Repository import ReservationRepository
from Repository import RoomRepository
from Schemas.Reservatios import Reservations as reservationSchema
from sqlalchemy.orm import Session

def Get(db: Session ):    
    reservationById = ReservationRepository.Get(db)
    return reservationById

def GetById( id:int ,db: Session ):    
    reservationById = ReservationRepository.GetById( id, db)
    return reservationById


def Add(reservation: reservationSchema, db: Session):  
    # ValidateId when (fishish the rest)    #   
   
    room =  RoomRepository.GetById( reservation.roomId ,db)
    if room is None:
        raise ValueError(status_code=404, detail="roomId don't exist in the Database")
    
    if not room.isAvailable:
        raise ValueError("Room is not available")

    # Validate date 
    isAvailable = ReservationRepository.ValidateDateReservation(reservation, db)
    if isAvailable is False:
        raise HTTPException(status_code=404, detail="Reservation is not available in that Date, change the dates")
    
    # validate if the available before to make a Reservation
    
    newReservation = ReservationRepository.Add(reservation, db)
    return newReservation

def Update(reservation: reservationSchema, db: Session):  
    # add condition for  reservation.id
    reservationUpdate = ReservationRepository.GetById( reservation.id, db)
    
    if reservationUpdate is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
        
    message = ReservationRepository.Update(reservation,reservationUpdate, db)

    return message

def Delete(id: int, db: Session):
  
    room = ReservationRepository.GetById( id, db)    
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
        
    message = ReservationRepository.Delete(room, db)

    return message
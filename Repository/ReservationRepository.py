from Schemas.Reservatios import Reservations as ReservationRespository
from Models.Reservation import Reservation as ReservationModel
from sqlalchemy.orm import Session


def Get(db: Session ):
     return db.query(ReservationModel).all()

def GetById(id:int ,db: Session ):
     return  db.query(ReservationModel).filter(ReservationModel.id == id).first()
           
def Add(reservation: ReservationRespository, db: Session ):
    newReservation = ReservationModel(**reservation.model_dump())
    db.add(newReservation)
    db.commit()
    db.refresh(newReservation)
    return newReservation

def ValidateDateReservation(reservation: ReservationRespository, db: Session ):
     return db.query(ReservationModel).filter(
        ReservationModel.roomId == reservation.roomId,
        (
            (ReservationModel.startDate < reservation.startDate) & (ReservationModel.endDate > reservation.startDate)
        ) | (
            (ReservationModel.startDate < reservation.endDate) & (ReservationModel.endDate > reservation.endDate)
        )
    ).count() == 0

def Update(reservation: ReservationRespository,reservationOriginal: ReservationRespository,  db: Session ):

    for key, value in reservation.dict().items():
            if hasattr(reservationOriginal, key):
                 setattr(reservationOriginal, key, value)

    db.commit()
    db.refresh(reservationOriginal)
    return reservationOriginal

def Delete(reservation: ReservationRespository,db: Session):
     db.delete(reservation)
     db.commit()

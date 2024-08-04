from fastapi import APIRouter, Depends, HTTPException , Body
from Services import ReservationService
from Schemas.Reservatios import Reservations as ReservationSchema
from config.database import  get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('')
def get(db: Session = Depends(get_db)):
        allRoom = ReservationService.Get(db)
        return allRoom


@router.get('/{id}')
def getByID( id: int ,db: Session = Depends(get_db)):
        room = ReservationService.GetById(id, db)     
        return room


@router.post('/')
def Post( reservationSchema: ReservationSchema = Body(...),
          db: Session = Depends(get_db)):
    try:       
        newRoom = ReservationService.Add(reservationSchema, db)
        return  newRoom
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put('/')
def put( reservationUpdate: ReservationSchema = Body(...),
         db: Session = Depends(get_db)):
        try:      
                reservationResult = ReservationService.Update(reservationUpdate, db) 
                return reservationResult
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
@router.delete('/{id}')
def Delete( id:int,
           db: Session = Depends(get_db)):  
        try:       
            ReservationService.Delete(id, db) 
            return "Delete complete"
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
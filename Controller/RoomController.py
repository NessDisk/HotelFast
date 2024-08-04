from fastapi import APIRouter, Depends, HTTPException , Body
from Services import RoomService
from Schemas.Room import Room as RoomSchema
from config.database import  get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('')
def get(db: Session = Depends(get_db)):
    allRoom = RoomService.Get(db)
    return allRoom


@router.get('/{id}')
def getByID( id: int ,db: Session = Depends(get_db)):
        room = RoomService.GetById(id, db)     
        return room


@router.post('/')
def Post( roomSchema: RoomSchema = Body(...), db: Session = Depends(get_db)):
    try:       
        newRoom = RoomService.Add(roomSchema, db)
        return newRoom
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put('/')
def put( roomUpdate: RoomSchema = Body(...),db: Session = Depends(get_db)):
        try:      
                roomResult = RoomService.Update(roomUpdate, db) 
                return roomResult
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
@router.delete('/{id}')
def Delete( id:int,db: Session = Depends(get_db)):  
        try:       
            RoomService.Delete(id, db) 
            return "Delete complete"
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
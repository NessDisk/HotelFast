from fastapi import HTTPException
from Repository import RoomRepository
from Schemas.Room import Room as RoomSchemas
from sqlalchemy.orm import Session

def Get(db: Session ):    
    newRoom = RoomRepository.Get(db)
    return newRoom

def GetById( id:int ,db: Session ):    
    newRoom = RoomRepository.GetById( id, db)
    return newRoom


def Add(room: RoomSchemas, db: Session):    
    newRoom = RoomRepository.Add(room, db)
    return newRoom

def Update(room: RoomSchemas, db: Session):    
    # add condition for  room.id
    newRoom = RoomRepository.GetById( room.id, db)
    
    if newRoom is None:
        raise HTTPException(status_code=404, detail="Room not found")
        
    roomUpdate = RoomRepository.Update(room,newRoom, db)

    return roomUpdate

def Delete(id: int, db: Session):
  
    room = RoomRepository.GetById( id, db)    
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
        
    message = RoomRepository.Delete(room, db)

    return message
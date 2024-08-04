from fastapi import HTTPException
from Repository import RoomRepository
from Schemas.Room import Room as RoomService
from sqlalchemy.orm import Session

def Get(db: Session ):
    
    newRoom = RoomRepository.Get(db)

    return newRoom

def GetById( id:int ,db: Session ):
    
    newRoom = RoomRepository.GetById( id, db)

    return newRoom


def Add(room: RoomService, db: Session):
    
    newRoom = RoomRepository.Add(room, db)

    return newRoom

def Update(room: RoomService, db: Session):
    # get room 
    newRoom = RoomRepository.GetById( room.id, db)
    
    if newRoom is None:
        raise HTTPException(status_code=404, detail="Room not found")
    
    # # update room 
    message = RoomRepository.Update(room,newRoom, db)

    return message


def Delete(id: int, db: Session):
    # get room 
    room = RoomRepository.GetById( id, db)
    
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    
    # # update room 
    message = RoomRepository.Delete(room, db)

    return message
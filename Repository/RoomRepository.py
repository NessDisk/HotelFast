
from Schemas.Room import Room as RoomRespository
from Models.Room import Room as RoomModel
from sqlalchemy.orm import Session


def Get(db: Session ):
     return db.query(RoomModel).all()

def GetById(id:int ,db: Session ):
     return  db.query(RoomModel).filter(RoomModel.id == id).first()
           
def Add(room: RoomRespository, db: Session ):
    newRoom = RoomModel(**room.dict())
    db.add(newRoom)
    db.commit()
    db.refresh(newRoom)
    return newRoom

def Update(room: RoomRespository,roomOriginal: RoomRespository,  db: Session ):

    for key, value in room.dict().items():
            if hasattr(roomOriginal, key):
                 setattr(roomOriginal, key, value)

    db.commit()
    db.refresh(roomOriginal)
    return roomOriginal

def Delete(room: RoomRespository,db: Session):
     db.delete(room)
     db.commit()

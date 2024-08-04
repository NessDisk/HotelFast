from fastapi import FastAPI , Body
from fastapi.responses import HTMLResponse
from Schemas.Reservatios import Reservations
from Controller import  ReservationController , RoomController
from config.database import Session, engine, Base
from Models.Reservation import Reservation as reservationModel
from Models.Room import Room as roomModel

app = FastAPI()
app.title = "HotelFast made with FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

reservations = [
    {
		"id": 1,
		"user": "Avatar",
		"room": "102",
		"dateStar": "2009/10/01",
		"dateEnd": "2009/10/02",
		"customerName": "Pedro"
	},
        {
		"id": 2,
		"user": "Alex",
		"room": "107",
		"dateStar": "2009/10/01",
		"dateEnd": "2009/10/02",
		"customerName": "Pedro"
	},
         {
		"id": 3,
		"user": "Alex2",
		"room": "108",
		"dateStar": "2009/10/05",
		"dateEnd": "2009/10/06",
		"customerName": "Sara"
	},
]



@app.get('/reservations_', tags=['reservation_'])
def get_Reservations():
    return reservations

@app.get('/reservations_/{id}', tags=['reservation_'])
def getByID_Reservations(id: int):
        for reserva in reservations:
            if reserva["id"] == id:
                return  reserva                
        return []

@app.get('/reservations_/', tags=['reservation_'])
def getQueryParants_Reservations(User: str, id: int):
             return "name: " + User + " + " + "id: " + str(id)


@app.post('/reservations_', tags=['reservation_'])
def Add_Reservaion(reservation: Reservations = Body(...)):
    reservations.append(reservation)
    return reservation

@app.put('/reservations_/{id}', tags=['reservation_'])
def put_Reservation(id:int,reservation: Reservations = Body(...)):
    for resva in reservations:
        if resva["id"] == id:
             resva["id"] = reservation.id
             resva["user"] = reservation.user
             resva["room"] = reservation.room
             resva["dateStar"] = reservation.dateStar
             resva["dateEnd"] = reservation.dateEnd
             resva["customerName"] = reservation.customerName
             
             return reservations
        
@app.delete('/reservations_/{id}', tags=['reservation_'])
def Delete_Reservation(id:int):  
     for resva in reservations:
        if resva["id"] == id:
            reservations.remove(resva)
        
            return reservations

   

app.include_router(ReservationController.router, prefix="/reservatios", tags=["reservation"])
app.include_router(RoomController.router, prefix="/rooms", tags=["rooms"])
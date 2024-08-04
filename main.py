from fastapi import FastAPI , Body
from fastapi.responses import HTMLResponse
from Schemas.Reservatios import Reservations
from Controller import  ReservationController , RoomController
from config.database import Session, engine, Base
from Models.Reservation import Reservation as reservationModel
from Models.Room import Room as roomModel

app = FastAPI()
app.title = "HotelFast made with FastAPI"
app.version = "0.1.0"

Base.metadata.create_all(bind=engine)
   

app.include_router(ReservationController.router, prefix="/reservatios", tags=["reservation"])
app.include_router(RoomController.router, prefix="/rooms", tags=["rooms"])
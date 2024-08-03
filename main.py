from fastapi import FastAPI , Body
from fastapi.responses import HTMLResponse
from Models.Reservatios import Reservations

app = FastAPI()
app.title = "HotelFast made with FastAPI"
app.version = "0.0.1"

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

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')



@app.get('/reservations', tags=['reservation'])
def get_Reservations():
    return reservations

@app.get('/reservations/{id}', tags=['reservation'])
def getByID_Reservations(id: int):
        for reserva in reservations:
            if reserva["id"] == id:
                return  reserva                
        return []

@app.get('/reservations/', tags=['reservation'])
def getQueryParants_Reservations(User: str, id: int):
             return "name: " + User + " + " + "id: " + str(id)


@app.post('/reservations', tags=['reservation'])
def Add_Reservaion(reservation: Reservations = Body(...)):
    reservations.append(reservation)
    return reservation

@app.put('/reservations/{id}', tags=['reservation'])
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
        
@app.delete('/reservations/{id}', tags=['reservation'])
def Delete_Reservation(id:int):  
     for resva in reservations:
        if resva["id"] == id:      
        
            return reservations

   
### Documentación proyecto - HotelFast
Este proyecto es una API RESTful construida con FastAPI para la administración de una aplicación de gestión de reservas de habitaciones. La API permite realizar operaciones Crear, Leer, Actualizar y Eliminar, tanto para las habitaciones como para las reservas. Las habitaciones pueden ser de tipo <individual>, <doble> o <suite>, y cada una tiene un precio por noche definido. Las reservas incluyen el nombre del cliente, la fecha de inicio y fin de la estancia, y están vinculadas a una habitación específica.

### Especificaciones Técnicas

  **1.  Modelos de Datos**

- Utiliza Pydantic para definir los modelos de datos.
- Define las tablas en SQLAlchemy.
- Validar las fechas de reserva para asegurar que no haya conflictos.
- Validar que la habitación esté disponible antes de crear una reserva.
1. **Validaciones**
    - Validar las fechas de reserva para asegurar que no haya conflictos.
    - Validar que la habitación esté disponible antes de crear una reserva.
### Tegnologias 
* Requisitos
* Python 3.8+
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite

### Inicializar

El proyecto está dentro de un entorno virtual de desarrollo por lo que primero se ejecuta el entorno, luego la instancias necesarias por ultimo se  ejecita 

Clonar el proyecto con el siguiente comando:

```bash
git clone https://github.com/NessDisk/HotelFast
```

## Nos movemos a la raíz del proyecto:
```bash
cd HotelFast
```

## Para activar el entorno virtual:
```bash
venv\Scripts\activate
```
## Instalar dependencias:
```bash
pip install -r requirements.txt
```
## Inicializar la Base de Datos
```bash
alembic upgrade head
```
## Ejecutar la aplicacion 
```bash
uvicorn main:app --reload
```
En caso de no funcionar el anterior usar el siguiente
```bash
python -m uvicorn main:app --reload
```
## Documentacion de Swagger

Para ver la documentacion con todos las entradas en el siguiente enlace 
```bash
http://localhost:8000/docs
```

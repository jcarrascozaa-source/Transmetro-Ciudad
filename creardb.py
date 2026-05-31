from app import app
from db import db

# IMPORTAR TODOS LOS MODELOS
from models.bus import Bus
from models.linea import Linea
from models.estacion import Estacion
from models.empleado import Empleado
from models.acceso import Acceso
from models.parqueo import Parqueo
from models.linea_estacion import LineaEstacion
from models.municipalidad import Municipalidad 

with app.app_context():

    db.create_all()

    print("Base de datos creada")
from flask import Blueprint
from flask import render_template

from models.bus import Bus
from models.estacion import Estacion
from models.linea import Linea
from models.empleado import Empleado

dashboard = Blueprint(
    'dashboard',
    __name__
)

@dashboard.route('/dashboard')
def ver_dashboard():

    total_buses = Bus.query.count()

    total_estaciones = Estacion.query.count()

    total_lineas = Linea.query.count()

    total_empleados = Empleado.query.count()

    buses_espera = 0

    for bus in Bus.query.all():

        if bus.estado_ocupacion() == "ESPERAR 5 MIN":

            buses_espera += 1

    estaciones_alerta = 0

    for estacion in Estacion.query.all():

        if estacion.alerta_ocupacion():

            estaciones_alerta += 1

    return render_template(
        'dashboard.html',
        total_buses=total_buses,
        total_estaciones=total_estaciones,
        total_lineas=total_lineas,
        total_empleados=total_empleados,
        buses_espera=buses_espera,
        estaciones_alerta=estaciones_alerta
    )
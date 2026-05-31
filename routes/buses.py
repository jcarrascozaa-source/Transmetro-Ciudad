from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.bus import Bus
from models.empleado import Empleado
from models.parqueo import Parqueo
from models.linea import Linea
from models.linea_estacion import LineaEstacion

from db import db

buses = Blueprint(
    'buses',
    __name__
)

# LISTAR
@buses.route('/buses')
def listar_buses():

    buses_db = Bus.query.all()

    pilotos = Empleado.query.filter_by(
        tipo='piloto'
    ).all()

    parqueos = Parqueo.query.all()

    lineas = Linea.query.all()

    return render_template(
        'buses.html',
        buses=buses_db,
        pilotos=pilotos,
        parqueos=parqueos,
        lineas=lineas
    )

# CREAR
@buses.route('/buses/crear', methods=['POST'])
def crear_bus():

    placa = request.form['placa']

    capacidad = int(request.form['capacidad'])

    pasajeros = int(request.form['pasajeros'])

    empleado_id = request.form['empleado_id']

    parqueo_id = request.form['parqueo_id']

    linea_id = request.form['linea_id']

    # CONTAR ESTACIONES DE LA LINEA
    cantidad_estaciones = LineaEstacion.query.filter_by(
        linea_id=linea_id
    ).count()

    # CONTAR BUSES DE LA LINEA
    cantidad_buses = Bus.query.filter_by(
        linea_id=linea_id
    ).count()

    # MAXIMO PERMITIDO
    maximo_buses = cantidad_estaciones * 2

    # VALIDAR MAXIMO
    if cantidad_buses >= maximo_buses:

        return "ERROR: Esta línea ya alcanzó el máximo de buses permitidos"

    nuevo_bus = Bus(
        placa=placa,
        capacidad=capacidad,
        pasajeros=pasajeros,
        empleado_id=empleado_id,
        parqueo_id=parqueo_id,
        linea_id=linea_id
    )

    db.session.add(nuevo_bus)

    db.session.commit()

    return redirect(
        url_for('buses.listar_buses')
    )

# ELIMINAR
@buses.route('/buses/eliminar/<int:id>')
def eliminar_bus(id):

    bus = Bus.query.get_or_404(id)

    db.session.delete(bus)

    db.session.commit()

    return redirect(
        url_for('buses.listar_buses')
    )
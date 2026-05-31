from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.estacion import Estacion
from models.municipalidad import Municipalidad
from models.empleado import Empleado

from db import db

estaciones = Blueprint(
    'estaciones',
    __name__
)

# LISTAR
@estaciones.route('/estaciones')
def listar_estaciones():

    estaciones_db = Estacion.query.all()

    municipalidades = Municipalidad.query.all()

    operadores = Empleado.query.filter_by(
        tipo='operador'
    ).all()

    return render_template(
        'estaciones.html',
        estaciones=estaciones_db,
        municipalidades=municipalidades,
        operadores=operadores
    )

# CREAR
@estaciones.route('/estaciones/crear', methods=['POST'])
def crear_estacion():

    nombre = request.form['nombre']

    capacidad = int(
        request.form['capacidad']
    )

    zona = request.form['zona']

    personas_actuales = int(
        request.form['personas_actuales']
    )

    municipalidad_id = request.form[
        'municipalidad_id'
    ]

    empleado_id = request.form[
        'empleado_id'
    ]

    nueva_estacion = Estacion(
        nombre=nombre,
        capacidad=capacidad,
        zona=zona,
        personas_actuales=personas_actuales,
        municipalidad_id=municipalidad_id,
        empleado_id=empleado_id
    )

    db.session.add(nueva_estacion)

    db.session.commit()

    return redirect(
        url_for('estaciones.listar_estaciones')
    )

# ELIMINAR
@estaciones.route('/estaciones/eliminar/<int:id>')
def eliminar_estacion(id):

    estacion = Estacion.query.get_or_404(id)

    db.session.delete(estacion)

    db.session.commit()

    return redirect(
        url_for('estaciones.listar_estaciones')
    )
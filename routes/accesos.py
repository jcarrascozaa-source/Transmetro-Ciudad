from flask import Blueprint, render_template, request, redirect, url_for

from models.acceso import Acceso
from models.estacion import Estacion
from models.empleado import Empleado

from db import db

accesos = Blueprint('accesos', __name__)

# LISTAR
@accesos.route('/accesos')
def listar_accesos():

    accesos_db = Acceso.query.all()

    estaciones = Estacion.query.all()

    guardias = Empleado.query.filter_by(
        tipo='guardia'
    ).all()

    return render_template(
        'accesos.html',
        accesos=accesos_db,
        estaciones=estaciones,
        guardias=guardias
    )

# CREAR
@accesos.route('/accesos/crear', methods=['POST'])
def crear_acceso():

    nombre = request.form['nombre']

    descripcion = request.form['descripcion']

    estacion_id = request.form['estacion_id']

    empleado_id = request.form['empleado_id']

    nuevo = Acceso(
        nombre=nombre,
        descripcion=descripcion,
        estacion_id=estacion_id,
        empleado_id=empleado_id
    )

    db.session.add(nuevo)

    db.session.commit()

    return redirect(
        url_for('accesos.listar_accesos')
    )

# ELIMINAR
@accesos.route('/accesos/eliminar/<int:id>')
def eliminar_acceso(id):

    acceso = Acceso.query.get_or_404(id)

    db.session.delete(acceso)

    db.session.commit()

    return redirect(
        url_for('accesos.listar_accesos')
    )
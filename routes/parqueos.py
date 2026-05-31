from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.parqueo import Parqueo
from models.estacion import Estacion

from db import db

print("PARQUEOS CARGADO")

parqueos = Blueprint(
    'parqueos',
    __name__
)

# LISTAR
@parqueos.route('/parqueos')
def listar_parqueos():

    parqueos_db = Parqueo.query.all()

    estaciones = Estacion.query.all()

    return render_template(
        'parqueos.html',
        parqueos=parqueos_db,
        estaciones=estaciones
    )

# CREAR
@parqueos.route('/parqueos/crear', methods=['POST'])
def crear_parqueo():

    nombre = request.form['nombre']

    capacidad = int(request.form['capacidad'])

    estacion_id = request.form['estacion_id']

    nuevo = Parqueo(
        nombre=nombre,
        capacidad=capacidad,
        estacion_id=estacion_id
    )

    db.session.add(nuevo)

    db.session.commit()

    return redirect(
        url_for('parqueos.listar_parqueos')
    )

# ELIMINAR
@parqueos.route('/parqueos/eliminar/<int:id>')
def eliminar_parqueo(id):

    parqueo = Parqueo.query.get_or_404(id)

    db.session.delete(parqueo)

    db.session.commit()

    return redirect(
        url_for('parqueos.listar_parqueos')
    )
from flask import Blueprint, render_template, request, redirect, url_for

from models.linea import Linea
from models.estacion import Estacion
from models.linea_estacion import LineaEstacion

from db import db

rutas_linea = Blueprint('rutas_linea', __name__)

# LISTAR
@rutas_linea.route('/rutas')
def listar_rutas():

    relaciones = LineaEstacion.query.all()

    lineas = Linea.query.all()

    estaciones = Estacion.query.all()

    return render_template(
        'rutas.html',
        relaciones=relaciones,
        lineas=lineas,
        estaciones=estaciones
    )

# CREAR
@rutas_linea.route('/rutas/crear', methods=['POST'])
def crear_ruta():

    linea_id = request.form['linea_id']

    estacion_id = request.form['estacion_id']

    orden = request.form['orden']

    distancia = request.form['distancia']

    nueva = LineaEstacion(
        linea_id=linea_id,
        estacion_id=estacion_id,
        orden=orden,
        distancia=distancia
    )

    db.session.add(nueva)

    db.session.commit()

    return redirect(url_for('rutas_linea.listar_rutas'))

# ELIMINAR
@rutas_linea.route('/rutas/eliminar/<int:id>')
def eliminar_ruta(id):

    relacion = LineaEstacion.query.get_or_404(id)

    db.session.delete(relacion)

    db.session.commit()

    return redirect(url_for('rutas_linea.listar_rutas'))
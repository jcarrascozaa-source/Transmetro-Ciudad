from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.linea_estacion import LineaEstacion
from models.linea import Linea
from models.estacion import Estacion

from db import db

linea_estaciones = Blueprint(
    'linea_estaciones',
    __name__
)

# LISTAR
@linea_estaciones.route('/linea_estaciones')
def listar_linea_estaciones():

    relaciones = LineaEstacion.query.all()

    lineas = Linea.query.all()

    estaciones = Estacion.query.all()

    return render_template(
        'linea_estaciones.html',
        relaciones=relaciones,
        lineas=lineas,
        estaciones=estaciones
    )

# CREAR
@linea_estaciones.route(
    '/linea_estaciones/crear',
    methods=['POST']
)
def crear_linea_estacion():

    linea_id = request.form['linea_id']

    estacion_id = request.form['estacion_id']

    orden = int(request.form['orden'])

    distancia = float(request.form['distancia'])

    nueva = LineaEstacion(
        linea_id=linea_id,
        estacion_id=estacion_id,
        orden=orden,
        distancia=distancia
    )

    db.session.add(nueva)

    db.session.commit()

    return redirect(
        url_for(
            'linea_estaciones.listar_linea_estaciones'
        )
    )

# ELIMINAR
@linea_estaciones.route(
    '/linea_estaciones/eliminar/<int:id>'
)
def eliminar_linea_estacion(id):

    relacion = LineaEstacion.query.get_or_404(id)

    db.session.delete(relacion)

    db.session.commit()

    return redirect(
        url_for(
            'linea_estaciones.listar_linea_estaciones'
        )
    )
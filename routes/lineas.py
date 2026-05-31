from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models.linea import Linea
from models.municipalidad import Municipalidad

from db import db

lineas = Blueprint(
    'lineas',
    __name__
)

# LISTAR
@lineas.route('/lineas')
def listar_lineas():

    lineas_db = Linea.query.all()

    municipalidades = Municipalidad.query.all()

    return render_template(
        'lineas.html',
        lineas=lineas_db,
        municipalidades=municipalidades
    )

# CREAR
@lineas.route('/lineas/crear', methods=['POST'])
def crear_linea():

    nombre = request.form['nombre']

    color = request.form['color']

    municipalidad_id = request.form['municipalidad_id']

    nueva_linea = Linea(
        nombre=nombre,
        color=color,
        municipalidad_id=municipalidad_id
    )

    db.session.add(nueva_linea)

    db.session.commit()

    return redirect(
        url_for('lineas.listar_lineas')
    )

# ELIMINAR
@lineas.route('/lineas/eliminar/<int:id>')
def eliminar_linea(id):

    linea = Linea.query.get_or_404(id)

    db.session.delete(linea)

    db.session.commit()

    return redirect(
        url_for('lineas.listar_lineas')
    )
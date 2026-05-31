from flask import Blueprint, render_template, request, redirect, url_for
from models.municipalidad import Municipalidad
from db import db

municipalidades = Blueprint('municipalidades', __name__)

# LISTAR
@municipalidades.route('/municipalidades')
def listar_municipalidades():
    municipios = Municipalidad.query.all()
    return render_template('municipalidades.html', municipios=municipios)

# CREAR
@municipalidades.route('/municipalidades/crear', methods=['POST'])
def crear_municipalidad():
    nombre = request.form['nombre']
    nuevo = Municipalidad(nombre=nombre)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('municipalidades.listar_municipalidades'))

# ELIMINAR
@municipalidades.route('/municipalidades/eliminar/<int:id>')
def eliminar_municipalidad(id):
    municipio = Municipalidad.query.get_or_404(id)
    db.session.delete(municipio)
    db.session.commit()
    return redirect(url_for('municipalidades.listar_municipalidades'))
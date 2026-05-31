from flask import Blueprint, render_template, request, redirect, url_for

from models.empleado import Empleado

from db import db

empleados = Blueprint('empleados', __name__)

# LISTAR
@empleados.route('/empleados')
def listar_empleados():

    empleados_db = Empleado.query.all()

    return render_template(
        'empleados.html',
        empleados=empleados_db
    )

# CREAR
@empleados.route('/empleados/crear', methods=['POST'])
def crear_empleado():

    nombre = request.form['nombre']

    dpi = request.form['dpi']

    telefono = request.form['telefono']

    direccion = request.form['direccion']

    nivel_educativo = request.form['nivel_educativo']

    tipo = request.form['tipo']

    nuevo = Empleado(
        nombre=nombre,
        dpi=dpi,
        telefono=telefono,
        direccion=direccion,
        nivel_educativo=nivel_educativo,
        tipo=tipo
    )

    db.session.add(nuevo)

    db.session.commit()

    return redirect(
        url_for('empleados.listar_empleados')
    )

# ELIMINAR
@empleados.route('/empleados/eliminar/<int:id>')
def eliminar_empleado(id):

    empleado = Empleado.query.get_or_404(id)

    db.session.delete(empleado)

    db.session.commit()

    return redirect(
        url_for('empleados.listar_empleados')
    )
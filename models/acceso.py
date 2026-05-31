from db import db

class Acceso(db.Model):

    __tablename__ = 'accesos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.String(200)
    )

    estacion_id = db.Column(
        db.Integer,
        db.ForeignKey('estaciones.id')
    )

    empleado_id = db.Column(
        db.Integer,
        db.ForeignKey('empleados.id')
    )
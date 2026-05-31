from db import db

class Empleado(db.Model):

    __tablename__ = 'empleados'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    dpi = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    telefono = db.Column(
        db.String(20)
    )

    direccion = db.Column(
        db.String(200)
    )

    nivel_educativo = db.Column(
        db.String(100)
    )

    tipo = db.Column(
        db.String(20)
    )
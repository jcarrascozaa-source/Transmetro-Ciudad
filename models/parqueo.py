from db import db

class Parqueo(db.Model):

    __tablename__ = 'parqueos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    capacidad = db.Column(
        db.Integer,
        nullable=False
    )

    estacion_id = db.Column(
        db.Integer,
        db.ForeignKey('estaciones.id')
    )
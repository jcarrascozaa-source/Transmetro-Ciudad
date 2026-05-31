from db import db

class LineaEstacion(db.Model):

    __tablename__ = 'linea_estacion'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    linea_id = db.Column(
        db.Integer,
        db.ForeignKey('lineas.id'),
        nullable=False
    )

    estacion_id = db.Column(
        db.Integer,
        db.ForeignKey('estaciones.id'),
        nullable=False
    )

    orden = db.Column(
        db.Integer,
        nullable=False
    )

    distancia = db.Column(
        db.Float,
        default=0
    )

    linea = db.relationship(
        'Linea',
        backref='linea_estaciones'
    )

    estacion = db.relationship(
        'Estacion',
        backref='linea_estaciones'
    )
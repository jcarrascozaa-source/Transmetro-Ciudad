from db import db

class Linea(db.Model):

    __tablename__ = 'lineas'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    color = db.Column(
        db.String(50),
        nullable=False
    )

    # MUNICIPALIDAD
    municipalidad_id = db.Column(
        db.Integer,
        db.ForeignKey('municipalidades.id')
    )

    municipalidad = db.relationship(
        'Municipalidad',
        backref='lineas'
    )

    def calcular_distancia_total(self):

        total = 0

        for relacion in self.linea_estaciones:

            total += relacion.distancia

        return total

    def __repr__(self):

        return f'<Linea {self.nombre}>'
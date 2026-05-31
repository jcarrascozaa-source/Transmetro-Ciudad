from db import db

class Estacion(db.Model):

    __tablename__ = 'estaciones'

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

    zona = db.Column(
        db.String(50)
    )

    personas_actuales = db.Column(
        db.Integer,
        default=0
    )

    # MUNICIPALIDAD
    municipalidad_id = db.Column(
        db.Integer,
        db.ForeignKey('municipalidades.id')
    )

    municipalidad = db.relationship(
        'Municipalidad',
        backref='estaciones'
    )

    # OPERADOR
    empleado_id = db.Column(
        db.Integer,
        db.ForeignKey('empleados.id')
    )

    empleado = db.relationship(
        'Empleado',
        backref='estaciones'
    )

    def alerta_ocupacion(self):

        try:

            capacidad = int(self.capacidad)

            personas = int(self.personas_actuales)

            return personas > (
                capacidad * 1.5
            )

        except:

            return False
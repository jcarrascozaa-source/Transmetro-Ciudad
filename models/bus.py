from db import db

class Bus(db.Model):

    __tablename__ = 'buses'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    placa = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    capacidad = db.Column(
        db.Integer,
        nullable=False
    )

    pasajeros = db.Column(
        db.Integer,
        default=0
    )

    # PILOTO
    empleado_id = db.Column(
        db.Integer,
        db.ForeignKey('empleados.id')
    )

    empleado = db.relationship(
        'Empleado',
        backref='buses'
    )

    # PARQUEO
    parqueo_id = db.Column(
        db.Integer,
        db.ForeignKey('parqueos.id')
    )

    parqueo = db.relationship(
        'Parqueo',
        backref='buses'
    )

    # LINEA
    linea_id = db.Column(
        db.Integer,
        db.ForeignKey('lineas.id')
    )

    linea = db.relationship(
        'Linea',
        backref='buses'
    )

    def estado_ocupacion(self):

        try:

            capacidad = int(self.capacidad)

            pasajeros = int(self.pasajeros)

            if pasajeros < (capacidad * 0.25):

                return "ESPERAR 5 MIN"

            return "NORMAL"

        except:

            return "NORMAL"
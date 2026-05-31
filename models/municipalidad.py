from db import db

class Municipalidad(db.Model):
    __tablename__ = 'municipalidades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Municipalidad {self.nombre}>'
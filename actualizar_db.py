from app import app
from db import db

with app.app_context():

    db.create_all()

    print("Base de datos actualizada")
from flask import Flask
from config import Config
from db import db

# CREAR APP
app = Flask(__name__)

# CONFIGURACIÓN
app.config.from_object(Config)

# INICIALIZAR BASE DE DATOS
db.init_app(app)

# IMPORTAR RUTAS
from routes.buses import buses
from routes.lineas import lineas
from routes.estaciones import estaciones
from routes.empleados import empleados
from routes.accesos import accesos
from routes.linea_estaciones import linea_estaciones
from routes.dashboard import dashboard
from routes.municipalidades import municipalidades

print("ANTES DE IMPORTAR PARQUEOS")

from routes.parqueos import parqueos

print("DESPUES DE IMPORTAR PARQUEOS")

# REGISTRAR BLUEPRINTS
app.register_blueprint(buses)
app.register_blueprint(lineas)
app.register_blueprint(estaciones)
app.register_blueprint(empleados)
app.register_blueprint(accesos)
app.register_blueprint(parqueos)
app.register_blueprint(linea_estaciones)
app.register_blueprint(dashboard)
app.register_blueprint(municipalidades)

# RUTA PRINCIPAL
from flask import redirect
from flask import url_for

@app.route('/')
def home():

    return redirect(
        url_for('dashboard.ver_dashboard')
    )

# EJECUTAR APP
if __name__ == '__main__':
    app.run(debug=True)
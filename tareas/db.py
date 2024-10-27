from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#El engine permite a SQLAlchemy comunicarse con la base de datos en un dialecto concreto
#https://docs.sqlalchemy.org/en/14/core/engines.html
engine = create_engine('sqlite:///database/tareas.db',
                       connect_args={"check_same_thread": False})
#Advertencia: Crear el engine, no conecta inmediatamente con la BD, eso lo hacemos luego.

#Ahora creamos la sesión, lo que nos permite realizar transacciones (operaciones) dentro de nuestra BD.
Session = sessionmaker(bind=engine)
session = Session()

#Ahora vamos al fichero models.py en los modelos (clases) donde queremos que se transformen en tablas,
# le añadiremos esta variable y esto se encargará de mapear y vincular cada clase a cada tabla.
Base = declarative_base()
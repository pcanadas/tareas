from sqlalchemy import Column, Integer, Boolean, String
import db

class Tarea(db.Base):

    __tablename__ = "tarea"
    __table_args__ = {'sqlite_autoincrement': True} # Autoincrementa la primary_key de la tabla.
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False) # Esto hace que el campo contenido NO pueda estar vacío.
    asignatura = Column(String(100), nullable=False) # Introducimos un campo para la categoría
    fecha = Column(Integer) #Introducimos un campo para la fecha límite
    hecha = Column(Boolean)

    def __init__(self, contenido, asignatura, fecha, hecha):
        self.contenido = contenido
        self.asignatura = asignatura
        self.fecha = fecha
        self.hecha = hecha
        print("Tarea creada con éxito")

    def __str__(self):
        return "Tarea {}: Asignatura {}, {}, {} ({})". format(self.id, self.asignatura, self.contenido, self.fecha, self.hecha)
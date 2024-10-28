from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

@app.route("/") # @ es un decorador que nos proporciona informacion extra de la función. / es el endpoint
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    return render_template("index.html", lista_de_tareas = todas_las_tareas) #Mandamos las variables

@app.route("/crear-tarea", methods=["POST"]) #Post referido a "Create", le puedo añadir otros métodos como GET (Read), PUT (Update)...
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], asignatura=request.form["asignatura_tarea"], fecha=request.form["fecha_tarea"], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home")) #Esto nos redirecciona a la función home()

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id))
    tarea.delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha) #Establecemos el estado contrario a tarea.hecha (es un boleano) - Invertimos el estado
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/editar-tarea/<id>", methods=['GET', 'POST'])
def editar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    print(tarea)
    tarea.asignatura=request.form["asignatura_editar"]
    tarea.contenido = request.form["contenido_editar"]
    tarea.fecha=request.form["fecha_editar"]

    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    # En la siguiente línea estamos indicando a SQLAlchemy que cree, si no existe, las tablas
    # de todos los modelos que encuentre en models.py
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True) # El debug=True hace que cada vez que reiniciemos el servidor, o modifiquemos el código, el
    #servidor de Flask se reinicie solo. Es un modo de producción que nos va a dar más datos. Al terminar habrá que quitarlo.

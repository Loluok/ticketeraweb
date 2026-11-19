import json
import csv

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_file,
    session,
    abort
)

from datetime import datetime

from roles import obtener_rol, tiene_permiso
from auth import login_required, permiso_requerido
from ldap_auth import autenticar_usuario
app = Flask(__name__)
app.secret_key = "clave-temporal-para-desarrollo"

@app.route("/")
def inicio():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    if not horario_permitido():
        return "Acceso denegado. Fuera del horario permitido.", 403

    usuario = request.form.get("usuario", "").strip().lower()
    password = request.form.get("password", "")

    if not autenticar_usuario(usuario, password):
        return render_template(
            "login.html",
            error="Usuario o contraseña incorrectos."
    ), 401

    rol = obtener_rol(usuario)

    if rol is None:
        return render_template(
            "login.html",
            error="Usuario no registrado en el sistema."
        ), 401

    session.clear()

    session["usuario"] = usuario
    session["rol"] = rol

    return redirect("/dashboard")


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        usuario=session["usuario"],
        rol=session["rol"],
        tiene_permiso=tiene_permiso
    )


@app.route("/crear_ticket", methods=["GET", "POST"])
@permiso_requerido("crear_ticket")
def crear_ticket():

    if request.method == "POST":

        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        prioridad = request.form["prioridad"]

        with open("data/tickets.json", "r") as archivo:
            tickets = json.load(archivo)

        nuevo_ticket = {
            "id": len(tickets) + 1,
            "titulo": titulo,
            "descripcion": descripcion,
            "prioridad": prioridad,
            "estado": "Abierto",
            "responsable": "Sin asignar",
            "comentarios": [],
            "historial": ["Ticket creado"],
        }

        tickets.append(nuevo_ticket)

        with open("data/tickets.json", "w") as archivo:
            json.dump(tickets, archivo, indent=4)

        return redirect("/dashboard")

    return render_template("crear_ticket.html")

@app.route("/tickets")
@permiso_requerido("ver_todos")
def ver_tickets():

    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    return render_template(
        "tickets.html",
        tickets=tickets
    )

@app.route("/estado/<int:id>", methods=["POST"])
@permiso_requerido("cambiar_estado")
def cambiar_estado(id):

    estado = request.form.get("estado")
    estados_permitidos = {"Abierto", "En Progreso", "Resuelto", "Cerrado"}

    if estado not in estados_permitidos:
        abort(400)

    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    ticket_encontrado = False

    for ticket in tickets:
        if ticket["id"] == id:

            ticket["estado"] = estado

            if "historial" not in ticket:
                ticket["historial"] = []

            ticket["historial"].append(
                f"Estado cambiado a {estado}"
        )

            ticket_encontrado = True
            break

    if not ticket_encontrado:
        abort(404)

    with open("data/tickets.json", "w") as archivo:
        json.dump(tickets, archivo, indent=4)

    return redirect("/tickets")

@app.route("/responsable/<int:id>", methods=["POST"])
@permiso_requerido("asignar_responsable")
def cambiar_responsable(id):

    responsable = request.form.get("responsable")

    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    for ticket in tickets:
        if ticket["id"] == id:

            ticket["responsable"] = responsable

            if "historial" not in ticket:
                ticket["historial"] = []

            ticket["historial"].append(
                f"Responsable asignado a {responsable}"
            )

        break

            

    with open("data/tickets.json", "w") as archivo:
        json.dump(tickets, archivo, indent=4)

    return redirect("/tickets")

@app.route("/comentario/<int:id>", methods=["POST"])
def agregar_comentario(id):

    comentario = request.form.get("comentario")

    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    for ticket in tickets:

        if ticket["id"] == id:

            if "comentarios" not in ticket:
                ticket["comentarios"] = []

            if comentario:
                ticket["comentarios"].append(comentario)

            break

    with open("data/tickets.json", "w") as archivo:
        json.dump(tickets, archivo, indent=4)

    return redirect("/tickets")

@app.route("/exportar_csv")
@permiso_requerido("exportar_csv")
def exportar_csv():
    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    with open("tickets.csv", "w", newline="") as archivo_csv:

        writer = csv.writer(archivo_csv)

        writer.writerow([
            "ID",
            "Titulo",
            "Descripcion",
            "Prioridad",
            "Estado",
            "Responsable",
    
        ])

        for ticket in tickets:
            writer.writerow([
                ticket["id"],
                ticket["titulo"],
                ticket["descripcion"],
                ticket["prioridad"],
                ticket["estado"],
                ticket.get("responsable", "Sin asignar"),
            ])

    return send_file(
        "tickets.csv",
        as_attachment=True
    )

def horario_permitido():
    #return True
    hora = datetime.now().hour
#descomentar el return para poder acceder :3
    return 8 <= hora < 21

@app.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

import json, csv
from flask import Flask, render_template, request, redirect, send_file
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    if not horario_permitido():
        return "Acceso denegado. Fuera del horario permitido."

    usuario = request.form["usuario"]
    password = request.form["password"]

    return render_template(
        "dashboard.html",
        usuario=usuario
    )

@app.route("/crear_ticket", methods=["GET", "POST"])
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
            "estado": "Abierto"
        }

        tickets.append(nuevo_ticket)

        with open("data/tickets.json", "w") as archivo:
            json.dump(tickets, archivo, indent=4)

        return "Ticket creado correctamente"

    return render_template("crear_ticket.html")

@app.route("/tickets")
def ver_tickets():

    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    return render_template(
        "tickets.html",
        tickets=tickets
    )

@app.route("/estado/<int:id>")
def cambiar_estado(id):

    with open("data/tickets.json", "r") as archivo:
        tickets = json.load(archivo)

    for ticket in tickets:

        if ticket["id"] == id:

            if ticket["estado"] == "Abierto":
                ticket["estado"] = "En Progreso"

            elif ticket["estado"] == "En Progreso":
                ticket["estado"] = "Resuelto"

            elif ticket["estado"] == "Resuelto":
                ticket["estado"] = "Cerrado"

    with open("data/tickets.json", "w") as archivo:
        json.dump(tickets, archivo, indent=4)

    return redirect("/tickets")

@app.route("/exportar_csv")
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
            "Estado"
        ])

        for ticket in tickets:
            writer.writerow([
                ticket["id"],
                ticket["titulo"],
                ticket["descripcion"],
                ticket["prioridad"],
                ticket["estado"]
            ])

    return send_file(
        "tickets.csv",
        as_attachment=True
    )

def horario_permitido():

    hora = datetime.now().hour

    return 8 <= hora < 18

if __name__ == "__main__":
    app.run(debug=True)


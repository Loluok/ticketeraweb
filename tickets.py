import json

ARCHIVO = "data/tickets.json"

def leer_tickets():

    with open(ARCHIVO, "r") as f:
        return json.load(f)

    def crear_ticket(ticket):

        tickets = leer_tickets()

        tickets.append(ticket)

    with open(ARCHIVO, "w") as f:
        json.dump(tickets, f, indent=4)


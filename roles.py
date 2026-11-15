roles = {
    "admin": "Admin",
    "juan": "Operador",
    "pedro": "Usuario",
    "maria": "Consulta"
}

def obtener_rol(usuario):
    return roles.get(usuario)
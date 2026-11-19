# Usuarios de prueba.

USUARIOS = {
    "admin": "Admin",
    "juan": "Operador",
    "pedro": "Usuario",
    "maria": "Consulta"
}


# Permisos por rol.

PERMISOS = {

    "Admin": [
        "crear_ticket",
        "ver_todos",
        "modificar_ticket",
        "cambiar_estado",
        "cambiar_prioridad",
        "asignar_responsable",
        "agregar_comentario",
        "consultar_historial",
        "exportar_csv"
    ],

    "Operador": [
        "ver_todos",
        "modificar_ticket",
        "cambiar_estado",
        "cambiar_prioridad",
        "asignar_responsable",
        "agregar_comentario",
        "consultar_historial",
        "exportar_csv"
    ],

    "Usuario": [
        "crear_ticket",
        "ver_propios",
        "agregar_comentario",
        "consultar_historial"
    ],

    "Consulta": [
        "ver_todos",
        "consultar_historial"
    ]
}


def obtener_rol(usuario):
    """Obtiene el rol correspondiente al usuario."""

    if not usuario:
        return None

    return USUARIOS.get(usuario.lower())


def tiene_permiso(rol, permiso):
    """Verifica si un rol posee determinado permiso."""

    return permiso in PERMISOS.get(rol, [])

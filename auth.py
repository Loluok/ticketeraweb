
from functools import wraps
from flask import session, redirect, abort

from roles import tiene_permiso


def login_required(func):
    """Exige que el usuario haya iniciado sesión."""

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "usuario" not in session:
            return redirect("/")

        return func(*args, **kwargs)

    return wrapper


def permiso_requerido(permiso):
    """Exige que el usuario tenga un permiso determinado."""

    def decorador(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if "usuario" not in session:
                return redirect("/")

            rol = session.get("rol")

            if not tiene_permiso(rol, permiso):
                abort(403)

            return func(*args, **kwargs)

        return wrapper

    return decorador

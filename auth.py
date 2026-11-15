from ldap3 import Server, Connection

def autenticar(usuario, password):

    server = Server("192.168.1.10")

    conn = Connection(
        server,
        user=f"EMPRESA\\{usuario}",
        password=password
    )

    return conn.bind()
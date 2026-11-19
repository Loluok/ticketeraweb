from ldap3 import Server, Connection


def autenticar_usuario(usuario, password):
    try:
        server = Server("192.168.56.101") # IP Q FUNCIONAA ADP 2

        conn = Connection(
            server,
            user=f"IFTS\\{usuario}",
            password=password
        )

        return conn.bind()

    except Exception as e:
        print("Error LDAP:", e)
        return False
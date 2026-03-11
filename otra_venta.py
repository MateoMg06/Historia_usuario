
si = True
no = False


def preguntar_otra_venta():
    respuesta = input("Deseas registrar otra venta? (s/n): ").strip().lower()

    if respuesta == "s" or respuesta == "si":
        return si

    return no

# Archivo: otra_venta.py
# Aqui preguntamos si el usuario quiere seguir.


# Guardamos los booleanos en variables
si = True
no = False


def preguntar_otra_venta():
    respuesta = input("Deseas registrar otra venta? (s/n): ").strip().lower()

    if respuesta == "s" or respuesta == "si":
        return si

    # Si no es s o si, se toma como no
    return no

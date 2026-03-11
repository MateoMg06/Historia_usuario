# Archivo: registrar_venta.py
# Aqui pedimos los datos de una venta.


def registrar_venta():
    # Pedimos el nombre del producto
    nombre = input("Nombre del producto: ")

    # Pedimos el precio y la cantidad (sin validaciones)
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))

    # Calculamos el subtotal
    subtotal = precio * cantidad

    # Guardamos todo en un diccionario
    venta = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal,
    }

    # Devolvemos la venta
    return venta


def registrar_venta():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))
    subtotal = precio * cantidad

    venta = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "subtotal": subtotal,
    }

    return venta

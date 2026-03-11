# Archivo: guardar_venta.py
# Aqui guardamos la venta y sumamos al total.


def guardar_venta(lista_ventas, venta, total_general):
    # Guardamos la venta en la lista
    lista_ventas.append(venta)

    # Sumamos el subtotal al total general
    total_general = total_general + venta["subtotal"]

    # Devolvemos el total actualizado
    return total_general

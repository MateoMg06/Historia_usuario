
def guardar_venta(lista_ventas, venta, total_general):
    lista_ventas.append(venta)
    total_general = total_general + venta["subtotal"]
    return total_general

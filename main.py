from inicializar import inicializar_variables
from registrar_venta import registrar_venta
from guardar_venta import guardar_venta
from otra_venta import preguntar_otra_venta
from mostrar_resumen import mostrar_resumen


def main():
    lista_ventas = inicializar_variables()
    total_general = 0

    si = True
    while si:
        venta = registrar_venta()
        total_general = guardar_venta(lista_ventas, venta, total_general)
        si = preguntar_otra_venta()

    mostrar_resumen(lista_ventas, total_general)


main()

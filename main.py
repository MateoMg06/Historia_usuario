from inicializar import inicializar_variables
from registrar_venta import registrar_venta
from guardar_venta import guardar_venta
from otra_venta import preguntar_otra_venta
from mostrar_resumen import mostrar_resumen


# Este programa sigue el diagrama de flujo paso a paso.
# Todo esta separado en funciones y en archivos diferentes.


def main():
    # Paso 1: crear la lista vacia
    lista_ventas = inicializar_variables()

    # Paso 1 (parte 2): crear el total en 0
    total_general = 0

    # Variable booleana para repetir
    si = True

    # Paso 2: repetir mientras el usuario quiera seguir
    while si:
        # Paso 3: pedir los datos de una venta
        venta = registrar_venta()

        # Paso 4: guardar la venta y sumar al total
        total_general = guardar_venta(lista_ventas, venta, total_general)

        # Paso 5: preguntar si hay otra venta
        si = preguntar_otra_venta()

    # Paso 6: mostrar el resumen final
    mostrar_resumen(lista_ventas, total_general)


# Ejecutamos el programa directamente
main()

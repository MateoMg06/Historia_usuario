
def mostrar_resumen(lista_ventas, total_general):
    print("RESUMEN")

    if lista_ventas == []:
        print("No hay ventas")
        print("Total", 0)
    else:
        numero = 1
        for venta in lista_ventas:
            print("Venta", numero)
            print("Producto", venta["nombre"])
            print("Precio", venta["precio"])
            print("Cantidad", venta["cantidad"])
            print("Subtotal", venta["subtotal"])
            numero = numero + 1

        print("Total", total_general)

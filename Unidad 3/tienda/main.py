from tienda.mi_tienda.tienda import Tienda

def mostrar_menu():
    print("\n Menú Principal")
    print("1. Agregar Producto")
    print("2. Registrar varios productos (*args)")
    print("3. Registrar un producto (**kwargs)")
    print("4. Mostrar Inventario")
    print("5. Calcular valor total del inventario")
    print("6. Aplicar descuento global")
    print("7. Salir")
    print("===============================")
    
def main():
    tienda = Tienda()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre del producto:")
            precio = float(input("Precio del producto:"))
            categoria = input("Categoría del producto:")
            cantidad = int(input("Cantidad del producto:"))
            tienda.agregar_producto(producto = tienda.registrar_productos(nombre = nombre, precio = precio, categoria = categoria, cantidad = cantidad))
        elif opcion == "2":
            n = int(input("¿Cuantos productos requiere agregar?: "))
            productos = []
            for i in range (n):
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                categoria = input("Categoria:")
                cantidad = int(input("Cantidad: "))
                productos.append((nombre,precio,categoria,cantidad))
            tienda.registrar_productos(*productos)
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del Producto: "))
            categoria = input("Categoria del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            tienda.registrar_productos(nombre=nombre, precio=precio,categoria=categoria, cantidad=cantidad)
        elif opcion == "4":
            tienda.mostrar_inventario()
        elif opcion == "5":
            tienda.calcular_valor_total()
        elif opcion == "6":
            porcentaje = float(input("Ingresa el porcentaje de descuento: "))
            tienda.agregar_descuento_global(porcentaje)
        elif opcion == "7":
            print("Saliendo...")
            break;
        else:
            print("Opción invalida, intente de nuevo por favor")

if __name__ == "__main__":
    main()
        
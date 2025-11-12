def menu():
    print("\n Menu:")
    print("1. Agregar Producto")
    print("2. Mostrar Menu")
    print("3. Buscar Producto")
    print("4. Calcular total")
    print("5. Salir")
    
def main():
    productos = []
    precios = []
    
    while True:
        menu()
        
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ").title()
            precio = float(input("Ingrese el precio del producto: "))
            productos.append(nombre)
            precios.append(precio)
            print(f"Producto '{nombre}' agregado con precio {precio}.")
        elif opcion == '2':
            if productos:
                print("\n Menú Actual:")
                for i in range(len(productos)):
                    print(f"{i + 1}. {productos[i]} - ${precios[i]:.2f}")
            else:
                print("No hay prooductos registrados.")
        elif opcion == '3':
            buscar = input("Ingrese el nombre del producto a buscar: ").title()
            if buscar in productos:
                index = productos.index(buscar)
                print(f"Producto encontrado: {productos[index]} - ${precios[index]:.2f}")
            else:
                print("Producto no encontrado")
        elif opcion == '4':
            #Calcular total con for
            total = 0
            for i in range(len(precios)):
                total = total + precios[i]
            print(f"El total de todos los productos es: ${total:.2f}")
            #Calcular total con SUM
            print(f"(Usando SUM) El total de todos los productos es: ${sum(precios):.2f}")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
main()
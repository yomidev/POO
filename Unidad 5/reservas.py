def menu():
    print("\n RESERVA DE VIAJES")
    print("1. Registrar reserva")
    print("2. Mostrar reserva")
    print("3. Buscar por destino")
    print("4. Calcular ingresos")
    print("5. Salir")
    
def main():
    pasajeros = []
    destinos = []
    precios = []
    
    while True:
        menu()
        opcion = int(input("Selecciona una opcion: "))
        
        if opcion == 1:
            nombre = input("Nombre del pasajero: ").title()
            destino = input("Nombre del destino").title()
            precio = float(input("Ingrese el costo del boleto: "))
            pasajeros.append(nombre)
            destinos.append(destino)
            precios.append(precio)
            print("Reserva realizada con exito")
        elif opcion == 2:
            print("\n Reservas registradas: ")
            for i in range(len(pasajeros)):
                print(f"{i+1} - Pasajero: {pasajeros[i]} - Destinos {destinos[i]} - Precio: {precios[i]}")
        elif opcion == 3:
            buscar = input("Ingresa el destino a buscar: ").title()
            encontrados = [i for i, d in enumerate(destinos) if d==buscar]
            if encontrados:
                print(f"Reservas hacia {buscar}: ")
                for i in encontrados:
                    print(f"{pasajeros[i]} - ${precios[i]}")
            else:
                print("No hay reservas registradas")
        elif opcion == 4:
            print(f"Ingresos totales: ${sum(precios)}")
        elif opcion == 5:
            print("Saliendo...")
            break
        else: 
            print("Opción no valida")

main()
        
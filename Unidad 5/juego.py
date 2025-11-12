def menu():
    print("\n Ranking de VideoJuegos")
    print("1. Agregar videojuego")
    print("2. Mostrar ranking")
    print("3. Mostrar estadisticas")
    print("4. Salir")
    
def main():
    juegos = []
    puntuaciones = []
    
    while True:
        menu()
        opcion = int(input("Selecciona una opcion (1-4): "))
        
        if opcion == 1:
            nombre = input("Ingrese el nombre del videojuego: ").title()
            if nombre in juegos:
                print("El juego ya se encuentra registrado")
                continue
            try:
                puntaje = int(input("Puntuacion (1-10): "))
                if 1 <= puntaje <= 10:
                    juegos.append(nombre)
                    puntuaciones.append(puntaje)
                    print("Videojuego agregado correctamente")
                else:
                    print("La puntación debe estar entre los valores de 1 y 10")
            except ValueError:
                print("Debes agregar un numero valido")
        elif opcion == 2:
            if juegos:
                print("\n Ranking de Videojuegos:")
                for j, p in sorted(zip(juegos, puntuaciones), key=lambda x: x[1], reverse=True):
                    print(f"{j}: {p}/10")
            else:
                print("No hay juegos registrados")
        elif opcion == 3:
            if puntuaciones:
                promedio = sum(puntuaciones) / len(puntuaciones)
                mejor = juegos[puntuaciones.index(max(puntuaciones))]
                peor = juegos[puntuaciones.index(min(puntuaciones))]
                print(f"\nEstadisticas:")
                print(f"Promedio de puntuaciones: {promedio:.2f}")
                print(f"Mejor videojuego: {mejor} con {max(puntuaciones)}/10")
                print(f"Peor videojuego: {peor} con {min(puntuaciones)}/10")
            else:
                print("No hay puntuaciones registradas")
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo")

main()
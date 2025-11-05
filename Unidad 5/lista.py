def menu():
    print("\n MENÚ PLAYLIST")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Mostrar Playlist")
    print("4. Buscar canción")
    print("5. Salir")
    
def main():
    playlist = []
    while True:
        menu()
        opcion = int(input("Seleccione una opción (1-5): "))
        if opcion == 1:
            cancion = input("Ingresa el nombre de la canción: ").title()
            if cancion in playlist:
                print("Esa canción ya existe en tu playlist")
            else:
                playlist.append(cancion)
                print("Canción agregada correctamente")
        elif opcion == 2:
            cancion = input("Ingrese la cancion que desea eliminar: ").title()
            if cancion in playlist:
                playlist.remove(cancion)
                print("Canción eliminada correctamente")
            else:
                print("La canción no se encuentra en la playlist")
        elif opcion == 3:
            if playlist:
                print("\n Tu Playlist")
                for i in range(len(playlist)):
                    print(f"{i + 1}. {playlist[i]}")
            else:
                print("Tu playlist esta vacia")
        elif opcion == 4:
            cancion = input("Ingrese el nombre de la canción a buscar: ").title()
            encontrado = False
            for i in range(len(playlist)):
                if cancion == playlist[i]:
                    encontrado = True
                    print("Cancion encontrada en la playlist; en el lugar", i)
                    break
            if encontrado == False:
                print("Canción no encontrada")
            #if cancion in playlist:
                #print("Canción encontrada en la playlist")
            #else: 
                #print("Canción no encontrada")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no valida, intente de nuevo")

main()
            
from clases.refugio import Refugio

def menu():
    refugio = Refugio()
    while True:
        print("Refugio de Mascotas \n")
        print("1. Registrar Mascota")
        print("2. Mostrar Mascotas")
        print("3. Saludar cuidador")
        print("4. Calcular edad humana")
        print("5. Adoptar mascota")
        print("6. Mostrar total de mascostas")
        print("7. Salir")
        
        opcion = input("Seleccionar una opcion: ")
        if opcion == "1":
            refugio.registrar_mascotas()
        elif opcion == "2":
            refugio.mostrar_mascotas()
        elif opcion == "3":
            nombre = input("Nombre de la mascota que saludara: ")
            persona = input("Nombre de la persona a saludar: ")
            for m in refugio.mascotas:
                if m.nombre.lower() == nombre.lower():
                    m.saludar(persona)
        elif opcion == "4":
            nombre = input("Nombre de la mascota: ")
            for m in refugio.mascotas:
                if m.nombre.lower() == nombre.lower():
                    print(f"Edad Humana aproximada: {m.edad_humano()} años")
        elif opcion == "5":
            refugio.adoptar()
        elif opcion == "6":
            Refugio.mostrar_total()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, intente de nuevo")

if __name__ == "__main__":
    menu()
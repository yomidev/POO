from animales.perro import Perro
from animales.gato import Gato
from animales.loro import Loro

def menu():
    print("Selecciona la opción a realizar:")
    print("1. Crear Perro")
    print("2. Crear Gato")
    print("3. Crear Loro")
    print("4. Mostrar todos los animales")
    print("5. Hacer que hablen y se muevan")
    print("6. Salir")
    
def main():
    animales = []
    while True:
        menu()
        opcion = input("Selecciona del 1 al 6: ")
        if opcion == "1":
            nombre = input("Nombre del perro: ")
            edad = int(input("Edad del perro: "))
            raza = input("Raza del perro: ")
            animales.append(Perro(nombre, edad, raza))
            print("Perro creado exitosamente.\n")
        elif opcion == "2":
            nombre = input("Nombre del gato: ")
            edad = int(input("Edad del gato: "))
            color = input("Color del gato:")
            animales.append(Gato(nombre, edad, color))
            print("Gato creado exitosamente.\n")
        elif opcion == "3":
            nombre = input("Nombre del loro: ")
            edad = int(input("Edad del loro: "))
            puede_hablar = input("¿Puede hablar? (s/n)").lower() == 's'
            animales.append(Loro(nombre, edad, puede_hablar))
            print("Loro creado exitosamente.\n")
        elif opcion == "4":
            if not animales:
                print("No hay animales creados.\n")
            else: 
                print("Lista de Animales: ")
                for i, animal in enumerate(animales, start=1):
                    print(f"{i}. {animal.mostrar_info}")
        elif opcion == "5":
            if not animales:
                print("No hay animales para interactuar")
            else:
                for animal in animales:
                    print(f"\n {animal.hablar()}")
                    print(f"\n {animal.moverse()}")
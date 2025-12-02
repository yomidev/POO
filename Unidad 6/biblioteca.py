import pickle
from datetime import datetime

catalogo = []

#Función para registrar los errores
def registrar_errores(mensaje):
    with open("errores.log", "a", encoding="utf-8") as log:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{fecha}] {mensaje}\n")
        
#Funcion para agregar libro
def agregar_libro():
    try: 
        print("\n Agregar Libro \n")
        titulo = input("Titulo: ").strip()
        autor = input("Autor: ").strip()
        genero = input("Genero: ").strip()
        while True:
            try:
                anio = int(input("Año de Publicación: "))
                break
            except: 
                print("Debe de ingresar un numero. Intente nuevamente")
        libro = {
            "titulo" : titulo,
            "autor" : autor,
            "genero" : genero,
            "año" : anio
        }
        catalogo.append(libro)
        with open("catalogo.txt", "a", encoding="utf-8") as cat:
            cat.write(f"{titulo};{autor};{genero};{anio}\n")
        print("Registro agregado correctamente")
    except Exception as e:
        registrar_errores(f"Error al agregar libro: {e}")
        print("Ocurrio un error revisa en el archivo de logs\n")

def mostrar_catalogo():
    print("\n Mostrar catalogo\n")
    try:
        with open("catalogo.txt", "r", encoding="utf-8") as cat:
            contenido = cat.read()
            if contenido.strip() == "":
                print("El archivo esta vacio\n")
            else:
                print(contenido)
    except FileNotFoundError:
        print("El archivo no existe\n")
    except Exception as e: 
        print(f"Error al mostrar catalogo: {e}")
        registrar_errores(f"Error al mostrar catalogo: {e}")
        
def buscar_libro():
    try:
        print("\n Buscar Libro\n")
        titulo_buscar = input("Titulo a buscar: ").lower().strip()
        encontrado = False
        
        for libro in catalogo:
            if libro["titulo"].lower == titulo_buscar:
                print("\nLibro Encontrado")
                print(f"Titulo: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Genero: {libro['genero']}")
                print(f"Año: {libro['año']}")
                encontrado = True
        if encontrado == False:
            print("El libro no existe")
    except Exception as e:
        registrar_errores(f"Error al buscar libro: {e}")
        print("Ocurrio un error")
        
def guardar_binario():
    try:
        with open("catalogo.bin", "wb") as f:
            pickle.dump(catalogo, f)
        print("Catalogo guardado correctamente")
    except Exception as e:
        registrar_errores(f"Error al guardar {e}")
        print("Error al guardar el archivo\n")
        
def cargar_binario():
    global catalogo
    try:
        with open("catalogo.bin", "rb") as f:
            catalogo = pickle.load(f)
        print("Catalogo cargado correctamente")
    except Exception as e:
        registrar_errores(f"Error al cargar archivo {e}")
        print("Ocurrio un error al cargar el archivo\n")
        
def exportar():
    try: 
        with open("export_catalogo.txt", "w", encoding="utf-8") as archivo:
            archivo.write("======CATALOGO DE LIBROS =======\n")
            for libro in catalogo:
                archivo.write(
                   f"Titulo: {libro['titulo']}\n Autor: {libro['autor']}\n Genero: {libro['genero']}\n Año de Publicación: {libro['año']}\n ---------------------------------------\n"
                )
            print("Archivo exportado correctamente")
    except Exception as e:
        registrar_errores(f"Error al exportar archivo: {e}")
        print("Ocurrio un error al exportar\n")
        
def main():
    while True:
        print("=====GESTOR DE BIBLIOTECA========")
        print("1. Agregar Libro")
        print("2. Mostrar Catalogo")
        print("3. Buscar Libro")
        print("4. Guardar Catalogo en binario")
        print("5. Cargar catalogo en binario")
        print("6. Exportar a archivo de texto")
        print("7. Salir")
        
        op = int(input("Ingresa una opción: "))
        if(op == 1):
            agregar_libro()
        elif(op == 2):
            mostrar_catalogo()
        elif(op == 3):
            buscar_libro()
        elif(op == 4):
            guardar_binario()
        elif(op == 5):
            cargar_binario()
        elif(op == 6):
            exportar()
        elif(op == 7):
            print("Saliendo")
            break
        else:
            print("Opcion invalida, intente nuevamente")

main()
        
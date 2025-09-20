class Libro:
    biblioteca = "Biblioteca Central" # Atributo de clase
    
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo # Atributo public
        self.autor = autor # Atributo public
        self._ejemplares = ejemplares # Atributo protected
        self.__prestados = 0 # Atributo private
        
    # Método public
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ejemplares: {self._ejemplares}")
        
    # Método protected
    def _mostrar_ejemplares(self):
        return self._ejemplares > 0
    
    # Método private
    def __registrar_prestamo(self):
        self._ejemplares -= 1
        self.__prestados += 1
        
    #Metodo public
    def prestar_libro(self):
        if self._mostrar_ejemplares():
            self.__registrar_prestamo()
            print(f"Se prestó el libro: {self.titulo}. Restan: {self._ejemplares} ejemplares.")
        else:
            print(f"No hay ejemplares disponibles del libro: {self.titulo}.")
            
    def historial(self):
        print(f"{self.titulo} ha sido prestado {self.__prestados} veces.")
        
libro1 = Libro("Dune", "Frank Herbert", 5)
libro2 = Libro("Juan Gaviota", "Richard Bach", 10)
libro3 = Libro("Percy Jackson", "Rick Riordan", 9)

libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()

libro1.prestar_libro()
libro1.prestar_libro()
libro1.prestar_libro()
libro1.prestar_libro()
libro1.prestar_libro()
libro1.prestar_libro()

libro1.historial()
libro2.historial()
libro3.historial()
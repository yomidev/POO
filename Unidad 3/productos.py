class Producto:
    lista_productos = []
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        Producto.lista_productos.append(self)

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")
    
    @classmethod
    def mostrar_inventario(cls):
        if not cls.lista_productos:
            print("No hay productos en el inventario.")
        else:
            print("Inventario de Productos:")
            for prod in cls.lista_productos:
                prod.mostrar_info()
    
    @classmethod
    def buscar_producto(cls, nombre):
        for prod in cls.lista_productos:
            if prod.nombre.lower() == nombre.lower():
                return prod
        return None
    
    @classmethod
    def eliminar_producto(cls, nombre):
        producto = cls.buscar_producto(nombre)
        if producto:
            cls.lista_productos.remove(producto)
            print("El producto ha sido eliminado")
        else:
            print("Producto no encontrado")
    
    @classmethod
    def agregar_producto(cls, nombre, precio, cantidad):
        return cls(nombre, precio, cantidad)
    
    def actualizar_datos(self, nuevo_precio=None, nueva_cantidad=None):
        if nuevo_precio is not None:
            self.precio = nuevo_precio
        if nueva_cantidad is not None:
            self.cantidad = nueva_cantidad
        print(f"El producto {self.nombre} ha sido actualizado")
        
    @classmethod
    def valor_total(cls):
        total = sum([p.precio * p.cantidad for p in cls.lista_productos])
        return total
    
def menu():
    while True:
        print("Menu de Inventario \n")
        print("1. Agregar Producto")
        print("2. Mostrar inventario")
        print("3. Buscar Producto")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Mostrar valor total")
        print("7. Salir")
        
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            nombre = input("Nombre del Producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))
            Producto.agregar_producto(nombre, precio, cantidad)
        
        elif opcion == "2":
            Producto.mostrar_inventario()
        
        elif opcion == "3":
            nombre = input("Ingresa el nombre del producto: ")
            resultado = Producto.buscar_producto(nombre)
            if resultado:
                resultado.mostrar_info()
            else:
                print("Producto no encontrado")
        
        
        
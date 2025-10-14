from .producto import Producto
class Tienda:
    nombre_tienda = "Python Store"
    
    def __init__(self):
        self.inventario = []
    
    def agregar_producto(self, producto):
        self.inventario.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda.")
     
    def registrar_productos(self, *args, **kwargs):
        if args:
            for datos in args:
                self.agregar_producto(Producto(*datos))
        if kwargs:
            self.agregar_producto(Producto(**kwargs))
            
    def mostrar_inventario(self):
        print(f"Inventario de la tienda {Tienda.nombre_tienda}:")
        if not self.inventario:
            print("No hay productos en el inventario.")
            return
        for producto in self.inventario:
            producto.mostrar_info()
    
    def calcular_valor_total(self):
        total = sum(p.precio * p.cantidad for p in self.inventario)
        print(f"Valor total del inventario: {total}")
        
    def agregar_descuento_global(self, porcentaje):
        if not self.inventario:
            print("No hay productos en el inventario para aplicar descuento.")
            return
        for p in self.inventario:
            p.aplicar_descuento(porcentaje)
            print("Descuento aplicado con éxito.")
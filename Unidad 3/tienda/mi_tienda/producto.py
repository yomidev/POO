class Producto:
    
    def __init__(self, nombre, precio, categoria, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}, Cantidad: {self.cantidad}")
        
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        print(f"Descuento aplicado a {self.nombre}. Nuevo precio: {self.precio}")
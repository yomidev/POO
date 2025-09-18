from datetime import datetime

class Agenda:
    def __init__(self):
        self.contactos = []
        
    def agregar_contacto(self, nombre, telefono, correo):
        try:
            if not telefono.isdigit():
                raise ValueError("El telefono debe de contener solo numeros")
            contacto = {
                "nombre" : nombre.title(),
                "telefono": telefono,
                "correo" : correo.lower(),
                "fecha_registro" : datetime.now()
            }
            self.contactos.append(contacto)
            print(f"Contacto: {nombre} fue agregado correctamente")
        except ValueError as e:
            print("Error: ",e)
            
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos registrados")
        else:
            print("\n Lista de Contactos:")
            for c in self.contactos:
                print(f"-{c['nombre']} // Tel: {c['telefono']} // Correo: {c['correo']} // Fecha de Registro: {c['fecha_registro']}")
                
    def eliminar_contacto(self, nombre):
        try:
            for c in self.contactos:
                if c["nombre"].lower() == nombre.lower():
                    self.contactos.remove(c)
                    print("El contacto fue eliminado")
                    return
                raise LookupError("No se encontro el contacto")
        except LookupError as e:
            print("Error: ", e)
            
agenda = Agenda()
agenda.agregar_contacto("Juanito", "5555555555", "juanito@gmail.com")
agenda.agregar_contacto("Carlos", "12345abc90", "carlos@mail.com")
agenda.agregar_contacto("Pedro", "11111111111", "pedro@mail.com")

agenda.listar_contactos()
agenda.eliminar_contacto("Pepito")
agenda.listar_contactos()

class CuentaBancaria:
    banco = "BBVA" #Atributo de clase
    def __init__(self, titular, saldo_inicial):
        self.titular = titular #Public
        self._saldo_inicial = saldo_inicial #Protected
        self.__nip = "1234" #Private
    
    #Public function
    def depositar(self, cantidad):
        self._saldo_inicial += cantidad
        print(f"Deposito exitoso. Saldo actual: {self._saldo_inicial}")
        
    #Protected function
    def _mostrar_saldo(self):
        print(f"El saldo de: {self.titular} = {self._saldo_inicial}")
    
    #Private function
    def __validar_nip(self, nip):
        return nip == self.__nip
    
    def retirar(self, cantidad, nip):
        if self.__validar_nip(nip):
            if cantidad <= self._saldo_inicial:
                self._saldo_inicial -= cantidad
                print(f"Retiro exitoso. Tu saldo actual es: {self._saldo_inicial}")
            else: 
                print("Fondos insuficientes")
        else:
            print("NIP incorrecto")
            
cuenta1 = CuentaBancaria("Pepito",1000)
print(cuenta1.titular)
print(cuenta1._saldo_inicial)
#print(cuenta1.__nip)

cuenta1.depositar(500)
cuenta1.retirar(300, "1234")
cuenta1.retirar(100, "0000")
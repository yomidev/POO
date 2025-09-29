class Calculadora:
    #Atributo de Clase:
    operaciones_totales = 0
    
    def __init__(self):
        self.resultado = 0
    
    
    def suma(self, a, b):
        Calculadora.operaciones_totales = Calculadora.operaciones_totales+1
        return a+b
    def resta (self, a, b):
        Calculadora.operaciones_totales = Calculadora.operaciones_totales+1
        return a-b
    def multiplicacion(self, a, b):
        Calculadora.operaciones_totales = Calculadora.operaciones_totales+1
        return a*b
    def division(self, a, b) -> int:
        if (b == 0):
            return None
        else:
            Calculadora.operaciones_totales = Calculadora.operaciones_totales+1
            return a/b
    
    @classmethod
    def num_operaciones(cls):
        print(f"El numero operaciones realizadas es: {cls.operaciones_totales}")
        
while True:
    calcular = Calculadora()
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa otro numero: "))
    operacion = input("Ingresa el simbolo de la operacion a realizar (+,-,*,/)")

    if (operacion == "+"):
        print("El resultado de la suma es: ", calcular.suma(a,b))
    elif (operacion == "-"):
        print("El resultado de la resta es: ", calcular.resta(a,b))
    elif (operacion == "*"):
        print("El resultado de la multiplicacion es: ", calcular.multiplicacion(a,b))
    elif(operacion == "/"):
        resultado = calcular.division(a,b)
        if (resultado == None):
            print("Error: No se puede dividir entre 0")
        else:
            print("El resultado de la division es: ", resultado)
    else: 
        print("Error: Operacion no valida")
    respuesta=int(input("Quiere continuar? 1=Si quiero continuar, 0=No "))
    if (respuesta==1):
        True
    else:
        print(Calculadora.num_operaciones())
        break

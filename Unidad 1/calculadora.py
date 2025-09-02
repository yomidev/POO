def sumar(a, b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def division(a,b):
    if b != 0: 
        return a/b
    else:
        return "Error: La division no se puede realizar"
    
def calculadora():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    operacion = input("Ingrese la operacion (+, -, *, /): ")

    if operacion == "+":
        resultado = sumar(num1,num2)
        print("El resultado de la suma es:", resultado)
    elif operacion == "-":
        resultado = restar(num1,num2)
        print("El resultado de la resta es:", resultado)
    elif operacion == "*":
        resultado = multiplicar(num1,num2)
        print("El resultado de la multiplicacion es:", resultado)
    elif operacion == "/":
        resultado = division(num1, num2)
        print("El resultado de la division es:", resultado)
    else:
        print("Error: Operacion no valida.")

calculadora()
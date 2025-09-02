print("Hola Mundo")

num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
operacion = input("Ingrese la operacion (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif operacion == "-":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif operacion == "*":
    resultado = num1 * num2
    print("El resultado de la multiplicacion es:", resultado)
elif operacion == "/":
    if num2 != 0:
        resultado = num1/num2
        print("El resultado de la division es:", resultado)
    else:
        print("Error: Division por cero no permitida.")
else:
    print("Error: Operacion no valida.")
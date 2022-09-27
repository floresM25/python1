def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion\n 1 - suma\n 2 -resta\n 3 - multiplicacion\n 4 - divicion\n 5 - salir\n "
    while True:
        opcion = int(input(massage))
        if opcion == 5:
            print("Bye")
            break 
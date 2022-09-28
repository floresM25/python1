def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion\n 1 - suma\n2 -resta\n3 - multiplicacion\n4 - division\n5 - salir\n "
    while True:
        opcion = int(input(message))
        #Comparar cada una de las opciones y llamar a la funcion que corresponda
        if opcion == 1:
            #Pedir numeros al usuario
            resultado_suma = suma(23, 54)
            print("El resultado de la suma es", resultado_suma)
        elif opcion == 2:
              #Pedir numeros al usuario
            resultado_resta = resta(23, 54)
            print("El resultado de la resta es: ", resultado_resta )
        elif opcion == 3:
              #Pedir numeros al usuario
            resultado_multi = multiply(23, 54)
            print("El resultado de la multiplicacion es: ", resultado_multi )
        elif opcion == 4:
              #Pedir numeros al usuario
            resultado_div = divide(23, 54)
            print("El resultado de la division es: ", resultado_div )


        if opcion == 5:
            print("Bye")
            break 
        else:
            print("Opcion Incorrecta")
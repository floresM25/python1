# Scrip que juega piedra papel o tijera con el usuario 
import random 

#Leer eleccion del Usuario 
user = input("Elige: Piedra, Papel o Tijera \n ")

# Generra eleccion de la maquina 
aleatorio = random.randint(1, 3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine ='papel'
else:
    machine = 'tijera'



# Comparar para determinar quien gana 
print(f"El usuario eligio {user} y la quina eligio {machine} ")
 
if machine == "piedra" and user == "tijeras":
    print("Gana machine")
elif  machine == "piedra" and user == "papel":
    print("Gana User")
elif  machine == "piedra" and user == "piedra":
    print("Empate")
elif  machine == "papel" and user == "tijera":
    print("Gana user")
elif  machine == "papel" and user == "piedra":
    print("Gana machine")
elif  machine == "papel" and user == "papel":
    print("Empate")
elif  machine == "tijera" and user == "tijera":
    print("Empate")
elif  machine == "tijera" and user == "piedra":
    print("Gana user")
elif  machine == "tijera" and user == "papel":
    print("Gana machine")



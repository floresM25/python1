#condicionles if elif else 
#nos permite evaluar expresiones booleanas que de cumplirse realizan 
# una accion y en caso de que no entonces realizan otra 

#Evaluar si una persona es mayor de edad
#Nos diga es niño, joven, adulto, bebe, muy mayor 
genero = input("Ingresa tu genero (H/M) : ")
age = int (input('Ingresa tu edad: ' ))

if genero == "H" : 

    if age <= 2:
        print("Eres un bebé!")
    elif age <= 12:
        print("Eres un niño")
    elif age <= 18:         
        print("Eres un Joven")
    elif age <= 50:
        print("Eres un Adulto")      
    elif age <= 60:
        print("Eres muy mayor!")
   
else:
    if age <= 2:
        print ("Eres una bebé!")
    elif age <= 12:
        print("Eres una niña")
    elif age <= 18:         
        print("Eres una Joven")
    elif age <= 50:
        print("Eres una Adulta")      
    elif age <= 60:
        print("Eres muy mayor!")




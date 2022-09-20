#Lee la edad de alguien 
#Resta 2 a esta edad y se llama last_years
#firts_years sera igual a los 2 por 10.5
#Multiplicar los años restantes (last_years) por 4
#Sumar los firts_years con el resultado anterior
#Imprimir lo siguiente "Tienes 24 años que equivalen a 78 años perrunos" 

edad_persona = int(input ("Ingresa tu edad "))
last_years = edad_persona - 2
firts_years = 2 * 10.5
last_years = last_years * 4 
edad_perro = last_years + firts_years
print(f"Tienes {edad_persona} años que equivalen a {edad_perro} años perrunos")
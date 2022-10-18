lista_elements = [
    {
        "id": 1,
        "Nombre": "Erik",
        "Apellido": "Flores"
    },
     {
        "Id": 2,
        "Nombre": "Fernando",
        "Apellido": "Castañeda"
    },
     {
        "Id": 1,
        "Nombre": "Oscar",
        "Apellido": "Guillen"
    },
     {
        "Id": 1,
        "Nombre": "Edwin",
        "Apellido": "Aquino"
    },
]



def add_element():
    # Lista_elementos.append()
    id = int(input('Ingresa el ID de la persona: '))
    name = input('Igresa el nombre de la persona: ')
    Apellido = input('Ingresar el apellido de la persona: ')
    persona = {
        'id': id,
        'nombre': Nombre,
        'apellido': Apellido
        
    }
    lista_elements.append(persona)
     
  

    

def remove_element():
    # for para buscar (puede buscar con un find )
    # Lista_elements.remove()
 id = int(input('Ingresa el ID del elemento a eliminar: '))
    found = find_elements(id)
    print(found)
    aceptar = input("Estas seguro? (S/N)")
    if aceptar == "S":
        lista_elements.remove(found)
        print("Elemento Eliminado") 


    

def find_element(id):
    # for para buscar
    found = {}
    for elemnt in lista_elements:
        if element['id'] == id :
            found = element
    return found 
    

def show_element():
    # for para interar y mostrar 
    for element in lista_elements:
        for key, value in element.items():
            print(f'{key} -> {value}') 
    

def edit_element():
    # for o find para buscar
    # editar 
    id = int(input('Ingresa el ID del elemento a editar: '))
    found = find_element(id)
    print(found) 



if __name___=='__main__':
    menu ='''
    Implementacion de CRUD de elementos:
    Elige una opcion
    1 - Insertar
    2 - Mostrar todos
    3 - Buscar por ID
    4 - Editar
    5 - Eliminar
    6 - Salir
    '''
    while True:
        opcion = input(menu)
        if opcion == '1':
            print("Insertar elemento")
            add_element()
        elif opcion == '2':
            print("Mostrar todos los elementos")
            show_elements()
        elif opcion == '3':
            print("Buscar por ID")
            id = int(input("Ingresar el ID a buscar: "))
            found = find_element(id)
            print(found) 
        elif opcion == '4':
            print("Editar elemento")
            edit_element()
        elif opcion == '5':
            print("Eliminar elemento")
        elif opcion =='6':
            print("BYE!")
            break 
        else:
            print("opcion incorrecta!")
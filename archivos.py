def leer_archivos(file):
    print(f'Intestas abrir etse archivo {file}')
    #abrir open() 
    #procesar read/write
    #cerrar close()
    #with nos permite agrupar el trabajo con archivos
    with open (file_name, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            print(linea)
       # while(linea):
        #    print(linea)
         #   linea = file.readline()

    #print('Archivo leido y cerrado')

def agregar_equipo(file_name,equipo):
    with open(file_name, 'a') as file:
        file.write(f"\n{equipo}")

    print("equipo guardado")

def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()

    try:
        lista_equipos.remove(equipo)
        print("Equipo eliminado")
            file.writelines(lista_equipos)
    except ValueError:
        print('El eqiopo que deseas eliminar no existe')

def actualizar_equipo(file_name,equipo, new_equipo):
    with open(file_name, 'r') as file:
       lista_equipos = file.readline()
    try:
        index_equipo = lista_equipos.index(f'{equipo}\n')
        lista_equipos[index_equipo] = new_equipo
        with open(file_name, 'w') as file:
    except ValueError:
        print("El equipo no se encontro")



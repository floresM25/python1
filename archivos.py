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
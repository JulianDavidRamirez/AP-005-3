'''
                 CREAR Y ESCRIBIR EN UN ARCHIVO

Para crear un nuevo archivo en Python, se usa el metodo open(), con uno de los siguientes parametros:
creara un archivo si el archivo especificado no existe  
"x" - Crear - creara un archivo, retorna un error si el archivo existe

"a" - Agregar (append) - creara un archivo si el archivo especificado no existe  

"w" - Escribir (Write) - creara un archivo si el archivo especificado no existe, se emplea para
                          escribir contenido en el archivo creado.                                            
           
Se creara un archivo empleando el parametro w y vamos a escribir el contenido:               
'''

file = open("manejoDeArchivos/demofile2.txt", "w")
file.write("Se creo el archivo demofile2.txt")
file.close()

file = open("manejoDeArchivos/demofile2.txt", "r")
print(file.read())

'''
# Para agregar contenido en un archivo existente:

file = open("manejoDeArchivos/demofile.txt", "a")
file.write("Este archivo tiene mas contenido")
file.close()

file = open("manejoDeArchivos/demofile.txt", "r")
print(file.read())

'''
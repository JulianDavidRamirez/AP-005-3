#    MANEJO DE ARCHIVOS

#* Rutas relativas = ubiacion relativa (especificar un archivo) en referencia al directorio actual
#* Rutas Absolutas = representa la ruta completa del recurso, parte del directorio raíz hasta llegar al archivo concreto

# Nota: si desea ejecutar la linea que quiere apreciar dicha acción, elimine el numeral "#", las lineas que empiezan por "#*" son notas de teoria.
#* Abrir un archivo mediante ruta relativa: 
f = open("manejoDeArchivos/demofile.txt", "r")

"""
Otra forma de abrir archivos mediante ruta absoluta:
f = open("D:/Julian/Documentos/Programación/manejoDeArchivos/demofile.txt", "r")
"""

print(f)
#* Leer el contenido del archivo:
# print(f.read())

#* Leer los cinco primeros caracteres del contenido del archivo:
# print(f.read(5))

#* Método readline(): lee una línea de archivo:
# print(f.readline())
# print(f.readline()) --> lee la segunda linea del archivo

#* Leer cada linea del archivo mediante un for:

for x in f:
    print(x)

f.close() # ---> cerrar el archivo despues de hacer las operaciones deseadas

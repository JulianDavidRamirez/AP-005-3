'''
          ELIMINAR ARCHIVOS

Import os : el modulo os permite acceder a funcionalidades dependientes del
Sistema Operativo. Sobre todo, aquellas que requieren de información sobre el 
entorno del mismo y permite manipular la estructura de directorios (para leer 
y escribir archivos)

Algunos métodos:

os.access(path, modo_de_acceso) --> Saber si se puede acceder a un archivo o directorio
os.getcwd() --> Conocer el directorio actual
os.chdir(nuevo_path) --> Cambiar de directorio de trabajo
os.chroot() --> Cambiar al directorio de trabajo raíz
os.chmod(path, permisos) --> Cambiar los permisos de un archivo o directorio
os.chown(path, permisos) --> Cambiar el propietario de un archivo o directorio
os.mkdir(path[, modo]) --> Crear un directorio
os.mkdirs(path[, modo]) --> Crear directorios recursivamente
os.remove(path) --> Eliminar un archivo
os.rmdir(path) --> Eliminar un directorio
os.removedirs(path) --> Eliminar directorios recursivamente
os.rename(actual, nuevo) --> Renombrar un archivo
os.symlink(path, nombre_destino) --> Crear un enlace simbólico

Este codigo comprueba si existe un archivo y lo elimina:
'''
import os 

if os.path.exists("manejoDeArchivos/demofile2.txt"): # demofile2.txt se crea en el archivo crearArchivo.py
    os.remove("manejoDeArchivos/demofile2.txt")
else:
    print("El archivo no existe.")
# LISTAS

my_lista = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde"]

print(my_lista)
print(type(my_lista))
print(my_lista[2])

print("Tamaño de la lista: ", len(my_lista))
print(my_lista[0:3])
print(my_lista[:2])

my_lista.append("Blanco")
print(my_lista)

my_lista.insert(3, "Negro")
print(my_lista)

my_lista.extend(["Marron","Gris"])
print(my_lista)

my_lista.remove("Marron")
print(my_lista)

my_lista.insert(8,"Marron")
print(my_lista)

print(my_lista.pop()) # Método pop: elimina y retoma un elemento de una lista
tamaño = len(my_lista)
# print(my_lista)
print("Tamaño de la lista: ",tamaño)

my_lista_3 = my_lista*3
print("Lista extendida: ", my_lista_3)
print("\n Sort::: \n ")
# my_lista.sort() ---> Otra manera de ordenar una lista
# print(my_lista)
my_listaSort= sorted(my_lista)
print(my_listaSort)

my_numList = [10,8,9,7,5,6,4,2,3,1]
my_numList.sort()
print("Lista ordenada de menor a mayor: ",my_numList)

my_numList.sort(reverse=True)
print("Lista ordenada de mayor a menor: ", my_numList)

# - - - - TUPLAS - - - - -

print("\n \t \t Tuplas")
my_tupla = tuple(my_lista)
print("\n Tupla:", my_tupla)

print(my_tupla[0])
print(my_tupla[2],"\n ")

# Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)

print("Rojo" in my_tupla)
print(my_tupla.count("Rojo")) # Método Count: devuelve un número entero que representa la cantidad de veces que aparece el valor en la lista

#Tupla con un solo elemento

my_tupla_unitaria = ("Blanco")
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin parentesis:

my_tupla = "Gaspar",5,8,1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables

nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
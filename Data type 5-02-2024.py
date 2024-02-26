# Tipo de datos 

print("\n \t Tipos de datos \n ")

x = 5
print(type(x))

x = "Hello world"
print(type(x))

x = 20.5
print(type(x))

x = ["apple","banana","cherry"]
print(type(x))

x = ("apple","banana","cherry")
print(type(x))

x = {"Name": "Julian","Age":"52"}
print(type(x))

x = 3+5j
print(type(x))

# Conversiones de datos 

print("\n \t Tipos de datos \n ")

x = 1
y = 2.8
z = 1j

# Convertir entero a float:
a = float(x)

# Convertir de float a entero:
b = int(y)

# Convertir de entero a complejo:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# ------------- VARIABLES --------------

print("\n \t Variables \n")

# Crear variables:

x = 5
y = "John"
print(x)
print(y)

x = 4       # x --> es de tipo int
x = "Sally" # x --> ahora es de tipo str
print(x)

# Casting:

x = str(3)    # x puede ser '3' --> str
y = int(3)    # y puede ser 3 --> int
z = float(3)  # z puede ser 3.0 --> float

# Una o doble cita: 

x = "John"
# es lo mismo como:
x = 'John'

# Las variables se puede destinguir de Mayusculas o minusculas (case-sensitive)
a = 4
A = "Sally"
# La variable A no sobrescribe a la variable a

# --- Nombre de las Variables
print("\n  Nombre de las Variables \n")

# Nombre legales para declarar variables:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Nombre ilegales para declarar variables:
"""
    2myvar = "John"
    my-var = "John"
    my var = "John"
"""
# Camel Case:
myVariableName = "John"
# Pascal Case:
MyVariableName = "John"
# Snake Case:
my_variable_name = "John"

# Declarar multiples variables:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Un valor para multiples variables:

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Desempaquetar:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# --- Nombre de las Variables
print("\n  Variables en Salida \n")

x = "Python is awesome"
print(x)

# Concadenar: 

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Otra forma:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Operacione matematicas:

x = 5
y = 10
print(x + y)

# Salida de varios tipos de datos:

x = 5
y = "John"
print(x, y)

# --- Variables Globales

print("\n  Variables Globales \n")

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Crear una variable adentro de la función:

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Palabra clave Global

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Palabra clave Global --> una palabra clave que permite a un usuario modificar una variable fuera del alcance actual.


# crear un numero random y almacenarlo en un archivo txt
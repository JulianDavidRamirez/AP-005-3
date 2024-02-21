#                   TUPLAS

frutas = ("apple", "banana", "cherry")
print(frutas)

# frutasDuplicadas = ("apple", "banana", "cherry", "apple", "cherry") ---> Permite duplicar valores en una tupla
# print(frutasDuplicadas)

print("Longitud de la tupla frutas:", len(frutas))

fruta = ("apple",) # ---> Crear una tupla con un solo valor
print(type(fruta))

frutasN = tuple(("apple", "banana", "cherry")) # ---> Utilizando el constructor tupla() para hacer una tupla
print(frutasN)

#             ACCESO A LAS TUPLAS
print()
print("Acceso a las tuplas: ")
print()

frutas = ("apple", "banana", "cherry")
print(frutas[1])
print(frutas[-1]) # ---> Negative index

frutas = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(frutas[2:5])
print(frutas[:4])
print(frutas[2:])
# Negative index
print(frutas[-4:-1])
# Verificar si un item existe dentro de la tupla
if "apple" in frutas:
  print("Yes, 'apple' is in the fruits tuple")

#               ACTUALIZAR TUPLAS

print()
print("Actualizar tuplas: ")
print()
x = ("carro", "moto", "bicicleta")
y = list(x)
y[1] = "avion"
x = tuple(y)
print(x)

tupla = ("apple", "banana", "cherry")
t = list(tupla)
t.append("orange")
tupla = tuple(t)
print(tupla)

# Otra manera con diferentes elementos: 

tupla = ("apple", "kiwi", "cherry")
t = ("mango",)
tupla += t
print(tupla)

# Eliminar elementos:

t = list(tupla)
t.remove("apple")
tupla = tuple(t)
print(tupla)

# Eliminar la tupla completa

del tupla
print(tupla) #Esto genera un error porque la tupla ya no existe
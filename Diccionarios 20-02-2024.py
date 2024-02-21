#    DICCIONARIO

print("DICCIONARIOS:")
print()
# Creación del primer diccionario:

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":1964
}
print(car)

# Consultar un item en un diccionario:
car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":1964
}
print(car["Brand"])

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":1964,
    "Year":2020
}
print(car)

print(len(car)) # Longitud del diccionario

# Diccionario con varios tipos de datos:
car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year":1964,
    "Color":["red", "white", "blue"]
}

# funcion type():

print(type(car))

# Constructor dict():

person = dict(Name = "Jhon", Age = 36, Country = "Norway")
print(person)

# Acceder al diccionario:

print()
print("Acceso al diccionario: ")
print()

# Acceso a un item del diccionario:

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

x = car["Model"]
print(x)

# Acceder a un item del diccionario con el método get():

x = car.get("Brand")
print(x)

# Método keys() --> Acceder a todas las claves dentro del diccionario

x = car.keys()
print(x)

# Añadir una clave en un diccionario

car["Color"] = "Blue"
print(x)

# Método values() --> Arroja todos los valores dentro del diccionario

x = car.values()
print(x)

# Cambiar un valor de una clave

car["Year"] = 2020
print(x)

car["Color"] = "Red"
print(x)

# Método items() --> Entrega la totalidad del diccionario, incluyendo claves y elementos

x = car.items()
print(x)

# Confirmar si la clave existe en un diccionario:

if "Model" in car:
    print("Yes, 'model' is one of the keys in the car diccionary")

# Método de update() --> Cambiar el vaor de una clave

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

car.update({"Year":2020})
print(car)

# Adiccionar una clave y un valor en un diccionario con el método update:

car.update({"Color": "Gray"})
print(car)

# Eliminar item en un diccionario:

print()
print("Eliminar items en un diccionario:")
print()

# Remover items, método pop()

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

car.pop("Model")
print(car)

# Método popitem() --> elimina el ultimo elemento del diccionario

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

car.popitem()
print(car)

# Método del

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

del car["Brand"]
print(car)

# Método clear() --> Elimina todos los elementos de un diccionario
car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

car.clear()
print(car)

# Diccionario en bucles

print()
print("Diccionarios en bucles")
print()

car = {
    "Brand":"Ford",
    "Model":"Mustang",
    "Year": 1964
}

for x in car:
    print(x)
print()
for x in car:
    print(car[x])
    
# Bucle con metodo values():
print()
for x in car.values():
    print(x)

# Bucle con metodo keys():
print()
for x in car.keys():
    print(x)

# Bucle con metodo items()
print()
for x,y in car.items():
    print(x,y)
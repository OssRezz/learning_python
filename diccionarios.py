config = {
    "url" : "https://www.hola.com",
    "key" : "123asdashdgasd",
    "username" : "Prueba",
    "password" : "12345",
}

print(config)

#Para acceder a un valor
print(config["url"])

#Para eliminar un valor de un diccionario
del config["username"]
print(config)

#Obtener las claves dentro de un diccionario
claves = config.keys()
print(claves)

#Para obtener los valores de un diccionario
values = config.values()
print(values)

#Si queremos separar los valores de un diccionario

items =  config.items()
print(items)

#agenda 
contacts = {
    "James" : {
        "number" : "12",
        "mail" : "James@mil.com",
    },
    "Bella" : {
        "number" : "34",
        "mail" : "Bella@mil.com",
    },
    "Perro" : {
        "number" : "56",
        "mail" : "Perro@mil.com",
    },
}

print(contacts["James"]["number"])
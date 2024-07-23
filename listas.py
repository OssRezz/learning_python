to_do = [
    "Ir al hotel",
    "Pedir un nuevo",
    "Comer HB",
    "Pedir un taxi de nuevo",
    "Entrar la habitación del hotel"
    ]

# Contar la cantidad de elementos
print(len(to_do))

#Acceder a un elementos indexado
print(to_do[0])

#Si queremos extaer desde un inicio y fin
print(to_do[0:2])


#Agregar un item a una lista
to_do.append("Ir por el avión")
print(to_do)

#Agregar un item en una posicion especifica
to_do.insert(3, "Comprar regalos")
print(to_do)

#Obtener la posicion de un elemento
print(to_do.index("Comprar regalos"))

numbers = [1,2,3,4,5,6,7,8,9,10]

#Obtener el numero mayor
print("Elemento mayor: ", max(numbers))

#Obtener el numero menor
print("Elemento min: ", min(numbers))


#Eliminar elementos de una lista
del numbers[0]
print(numbers)

#Para conocer el id en memoria de una lista, usamos id

a = [1,2,3,4,5]
b = a

del a[0]

print(id(a))
print(id(b))



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
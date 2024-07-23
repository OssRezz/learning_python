

#Lista
my_list = [1, 2, 3, 4, 5, 6]

#Obtener el iterador
my_iter = iter(my_list)

for number in my_iter :
    print(number)
    
    
#Crear un iterador para los numeros impares

limit = 10

odd_itter = iter(range(1, limit + 1, 2))

#for num in odd_itter :
#   print(num)
    
    
#Generador 

def my_generator():
    yield 1
    yield 2
    yield 3
    
for values in my_generator():
    print(values)
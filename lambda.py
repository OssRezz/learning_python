def add(a, b): return a + b


print(add(10, 4))


def multiply(a, b): return a * b


print(multiply(10, 4))


# Obtener cuadrado de cada nuero

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))


print(numbers)
print(squared_numbers)


# Obtener numeros pares

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
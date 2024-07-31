# Funciones Lambda y programación funcional en Python

## Funciones

Para crear una función, la sintaxis es:

```
def Saludar(nombre):
    return "Hola " + nombre
    
print(Saludar("James"))
```

## Lambda (Funciones anonimas)

- Lambda nos permite crear codigo mas corto y simple, para realizar diferentes operaciones.

Para crear una función lambda, la sintaxis es:

```
# Realizar la suma de dos numeros

def add(a, b): return a + b
print(add(10, 4))

```


```
# Obtener cuadrado de cada nuero

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))

```

## Funciones recursivas 

Es una función que se llama asi misma hasta finalizar una operación

Para crear una función recursiva, la sintaxis es:

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

```
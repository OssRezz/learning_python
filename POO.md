# POO - Programación orientada a objectos

## Clases

Usamos la palabra reserva class para crear una clase, la sintaxis es:

```

class Cat:
    # Para crear un constructor tenemos la siguiente sintaxis
    # El constructor debe llamarse asi mismo con selft
    # Luego de self declaramos las variables que contiene la clase
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Constructor

Para crear un constructor tenemos la siguiente sintaxis:

1. El constructor debe llamarse asi mismo con selft
2. Luego de self declaramos las variables que contiene la clase

```
class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def miau(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")
```

## Usar una clase

Para instalar la clase, ponemos el nombre de la clase y dentro de esta los parametros establecidos en el contructor.

Luego por medio de la variable asignada la clase, podemos ejecutar las diferentes metodos de nuestra clase

```
Chloe = Cat("Chloe", 2)
Bella = Cat("Bella", 1)
Perro = Cat("Perro", 7)
Perrito = Cat("Perrito", 5)


Chloe.miau()
Bella.miau()
Perro.miau()
Perrito.miau()
```
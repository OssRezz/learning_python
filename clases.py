# Usamos la palabra reserva class para crear una clase
class Cat:
    # Para crear un constructor tenemos la siguiente sintaxis
    # El constructor debe llamarse asi mismo con selft
    # Luego de self declaramos las variables que contiene la clase
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def miau(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")


Chloe = Cat("Chloe", 2)
Bella = Cat("Bella", 1)
Perro = Cat("Perro", 7)
Perrito = Cat("Perrito", 5)


Chloe.miau()
Bella.miau()
Perro.miau()
Perrito.miau()


class Car:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        self.active = True

    def CanBeSold(self, date):
        if self.active:
            print(f"The car {self.name} can be sold in the date {date}")
        else:
            print(f"The car can't be sold in the date {date}")


car = Car("Manza 6", "red")

car.CanBeSold("Tomorrow")

def add(numero_uno, numero_dos):
    return numero_uno + numero_dos


def subtract(numero_uno, numero_dos):
    return numero_uno - numero_dos


def divide(numero_uno, numero_dos):
    return numero_uno / numero_dos


def multiply(numero_uno, numero_dos):
    return numero_uno * numero_dos


def operations():
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")


def calculator():
    operations()

    option = input("Type the operation you want: ")

    if option not in ["1", "2", "3", "4"]:
        print("<--------------------------->")
        print("You have to tpye 1, 2, 3, 4 ")
        print("<--------------------------->")
        operations()
        option = input("Type the operation you want: ")

    number_one = input("Type the first number: ")
    number_two = input("Type the second number: ")

    if number_one.isdigit() and number_two.isdigit():
        number_one = int(number_one)
        number_two = int(number_two)
    else:
        print("<--------------------------->")
        print("The number have to be an integer")
        print("<--------------------------->")
        operations()
        option = input("Type the operation you want: ")

    result = 0
    operationsDictionary = {
        1: "Add",
        2: "Subtract",
        3: "Divide",
        4: "Multiply",
    }

    if option == "1":
        result = add(number_one, number_two)
    elif option == "2":
        result = subtract(number_one, number_two)
    elif option == "3":
        result = divide(number_one, number_two)
    elif option == "4":
        result = multiply(number_one, number_two)

    print("The result of " +
          operationsDictionary[int(option)] + " is:", result)


calculator()

import random


def Draw(intento):
    etapas = [
        """
           -----
           |   |
               |
               |
               |
               |
        ========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========
        """
    ]

    print(etapas[intento])

# 6 Intentos


def Words():
    word = [
        "amistad",
        "aventura",
        "biblioteca",
        "chocolate",
        "felicidad",
        "galaxia",
        "jirafa",
        "koala",
        "mariposa",
        "naturaleza",
        "quimera",
        "serenidad",
        "tranquilidad",
        "universo",
        "ventana",
        "yogur",
        "zanahoria"
    ]

    return random.choice(word)


def hanged():
    word = Words()
    word_quantity = len(word)
    attempts = 0
    failed_attempts = 0
    correct = 0
    word_to_replace = ['_'] * word_quantity

    dic_test = {
        "word": word,
        "word_replace": list(word),
        "replace": list(word_to_replace),
        "word_to_search": word
    }

    while True:
        character = input("Type one character: ")

        while len(character) > 1:
            print("\nYou can only type one character!")
            character = input("Type one character: ")

        print("\n")

        if failed_attempts == 6:
            Draw(failed_attempts)
            print("\n")
            print("YOU ARE DEAD!")
            print("The word was: ", dic_test["word"])
            break

        if character not in dic_test["word_to_search"]:
            failed_attempts = failed_attempts + 1
            result = False
        else:
            dic_test["replace"][dic_test["word_to_search"].find(
                character)] = character
            dic_test["word_replace"][dic_test["word_to_search"].find(
                character)] = "!"
            dic_test["word_to_search"] = ''.join(dic_test["word_replace"])
            result = True
            correct = correct + 1

        attempts = attempts + 1
        Draw(failed_attempts - 1)
        print("Attemps: ", attempts)
        print("Correct!") if result else print("Failed!")
        print("\n")
        print(' '.join(dic_test["replace"]))
        if correct == word_quantity:
            print("Congratulations, you are the best")
            break


hanged()

# Python

- Python fue creado em 1991 por Guido Van Rossum, siguiendo una filosofia de simplicidad.


### Características Principales:
- El codigo se ejecuta de arriba a abajo y de izquierda a derecha
- Python es de alto nivel
- Paradgimas POO y programacion funcional
- Sintaxis Clara: Fácil de leer y escribir, lo que lo hace ideal para principiantes.
- Tipado Dinámico: No es necesario declarar el tipo de variable, lo que facilita la programación.
- Multiplataforma: Compatible con Windows, macOS y Linux
- Extensa Biblioteca Estándar: Ofrece muchas funciones y módulos listos para usar.
- Comunidad Activa: Gran cantidad de recursos, tutoriales y foros de ayuda.
- Usos Comunes:
    - Desarrollo Web: Frameworks como Django y Flask.
    - Ciencia de Datos: Bibliotecas como Pandas y NumPy.
    - Inteligencia Artificial y Machine Learning: Herramientas como TensorFlow y Scikit-learn.
    - Automatización: Scripts para tareas repetitivas.
    - Desarrollo de Juegos: Uso de bibliotecas como Pygame.


## Inslatación de Python

- En ubuntu viene por defecto al isntalar, en caso de que no sea asi usamos el siguiente comando para instalar:
  
  1.  Abrimos la terminal
  2.  Escribimos el comando sudo apt update
  3.  Escribimos el comando sudo apt install python3
  4.  Validamos que python exista en nuestra consola con el comando python3 --version

- En windows:
  
    1. Abrimos el sgt enlance: https://www.python.org/downloads/
    2. Precionamos en descargar
    3. Ejecutamos el .exe y seguimos los pasos de instalación

Si en la consola escribimos python, este ya nos permite usar el interprete de Python, por lo tanto si escribimos print("Hola mundo"), obtendremos la respuesta en la consola.

## Ejecutar archivos desde la consola

1. Nos movemos a la carpeta donde se encuentra el archivo
2. Escribimos python3 nombre_archivo.py 
3. Vemos en resultado en la consola


## Identación de codigo en Python

- Python es muy sensabile respecto a la identación, por ende requiere tener un codigo muy organizado y estructurado.

- Identación correcta:

    ```
    print("hola")
    print("mundo")
    ```

    Este imprimirá correctamente.

- Identación incorrecta:

    ```
    print("hola")
        print("mundo")
    ```
    Este codigo nos va a presentar el siguiente error: **_IndentationError: unexpected indent_**

## Comentarios en python

- Para comentar en python una linea de codigo usamos #

## Variables en Python

### Sintaxis

- Nombre de la variable
- Para inicializar una variable va el nombre y la asginación de valor
- Para un string, debemos ponerlo dentro de comillas 
  
    ```
    learning = "Python"
    ```

- Si es un numero, debemos ponerlo como numero sin comillas
  
    ```
    numero = 10
    ```

- Si es un decimal(float), debemos ponerlo sin comillas
  
    ```
    numero = 10.258
    ```

- Si es un boolean (falso - verdadero) es requerido que al ser declarado false o true, sea en mayuscula, dado que esta es una variable reservada del sistema
  
    ```
    is_true = True
    is_false = False

    print(is_true)
    print(is_false)
    ```

    Si la ponemos con la inicial minuscula esta nos dará un error



### Reglas

- Una variable no puede comenzar por numeros
- Una variable no puede comenzar por palabras reservadas como: class, function etc..
- Una variable no puede comenzar por un simbolo

## Operaciones matematicas en Python

- Cuando ejecutamos una operación con diferentes calculos, se utiliza PEMDAS, la cual estipula el ordne de ejecución de la formula:

    - P parentheses
    - E Exponents
    - M multiply
    - D Divide
    - A Add
    - S subtract
  
    ```
    operation_one = 2 + 3 * 4 
    operation_two = 2 + (3 * 4) 

    print('Operaticíon 1: ', numero_uno)
    print('Operaticíon 2: ', operation_two)   
    ```

    Operaticíon 1:  12

    Operaticíon 2:  14


## Manipulación de Strings en Python

- Podemos declarar un string con varios tipos de comillas
    ```
    learning = "Python"
    learning = 'Python'
    learning = '''Python
    
    Es un lenguaje de programación
    '''
    ```

    En este caso cuando usamos 3 comillas simples, nos permite reflejar saltos de lineas en un string.

- Si queremos obtener un caracter de un string:
  
    ```
    learning = "Python"
    print(learning[0])    
    ```

    En este caso obtenemos la primera posicion que seria el caracter "P", si en vez de 0, ingresamos 1, obtendremos el caracter "y".

    En caso de poner un numero que no este dentro de la cadena, saldrá el error "string index out of range"

- Si queremos obtener el ultimo caracter del string

  
    ```
    learning = "Python"
    print(learning[-1])    
    ```
    En este caso el caracter retornado será el ultimo, en este caso "n" y pones -2, nos va a retornar la "o" y así sucesivamente.

- Concatenación strings

  
    ```
    nombre = "James"
    Apellido = "Osorio FLorez"

    print(nombre + ' ' + Apellido)   
    ```

    En este caso el valor retornado es "James Osorio Florez"

- Operaciones Matematicas con un string

    ```
    nombre = "James"
    print(nombre * 5)   
    ```

    En este caso el valor retornado será: "JamesJamesJamesJamesJames"

- Conocer la longitud de un String

    ```
    nombre = "James"
    print(len(nombre))   
    ```
    En este caso nos va retorna 5, que son la cantidad de caracteres en el string.

- lower, nos permite volver un string a minuscula

    ```
    nombre_mayus = "JAMES"
    print("JAMES a minucula: " + nombre_mayus.lower())
    ```
    En este caso el retorno sera "james"

- upper, nos permite volver un string a mayuscula

    ```
    nombre_mayus = "james"
    print("james a mayuscula: " + nombre_minus.upper())
    ```
    En este caso el retorno sera "JAMES"

- strip, eLiminar espacio del principio y final de un string

    ```
    nombre_spaces = "       james         "
    print("Variable sin espacios: " + nombre_spaces.strip())
    ```
    En este caso el retorno será sin espacios al inicio y final, pero va a mantener los que estan dentro del primer y ultimo caracter

<!-- ## Manipulación de Strings en Python


 -->


## Listas en Python

- La sintaxis de la lista es:
  
    ```
    to_do = [
    "Ir al hotel",
    "Pedir un nuevo",
    "Comer HB",
    "Pedir un taxi de nuevo",
    "Entrar la habitación del hotel"
    ]
    ```

- La lista puede cualquier tipo de dato, mixto o unicos.
  
- Para conocer cuantos elemenos tiene una lista, podemos un len
  
    ```
    to_do = [
    "Ir al hotel",
    "Pedir un nuevo",
    "Comer HB",
    "Pedir un taxi de nuevo",
    "Entrar la habitación del hotel"
    ]

    print(len(to_do))

    ```

    El retorno en este caso seria 5, a diferencia de otros lenguajes de programación python comienza de 1 en adelante, no desde 0 al usar la funcíon len

- Para acceder a un elemento indexado
  
    ```
    to_do = [
    "Ir al hotel",
    "Pedir un nuevo",
    "Comer HB",
    "Pedir un taxi de nuevo",
    "Entrar la habitación del hotel"
    ]

    #Acceder a un elementos indexado
    print(to_do[0])
    ```

    Para acceder a un array, Python comienza desde 0, por ende si queremos acceder a la primera posición, debemos indexar el valor de 0, para este caso el return seria "Ir al hotel"

    En caso de querer el ultimo item, podemos ingresar [-1]
- Para acceder a un elemento indexado
  
    ```
    to_do = [
    "Ir al hotel",
    "Pedir un nuevo",
    "Comer HB",
    "Pedir un taxi de nuevo",
    "Entrar la habitación del hotel"
    ]

    #Si queremos extaer desde un inicio y fin
    print(to_do[0:2])
    ```

    Con esto extraemos cierta cantidad de valores dentro de un array, un inicio y fin, el valor a retornar será ['Ir al hotel', 'Pedir un nuevo']

    No es necesario poner 0, lo podemos dejar sin contenido y Python ya entiende que va desde 0

- Para agregar un item a una lista, usamos .append

    ```
    to_do = [
    "Ir al hotel",
    "Pedir un nuevo",
    "Comer HB",
    "Pedir un taxi de nuevo",
    "Entrar la habitación del hotel"
    ]

    #Agregar un item a una lista
    to_do.append("Ir por el avión")
    print(to_do)
    ```
    El resultado que va a retornar es: ['Ir al hotel', 'Pedir un nuevo', 'Comer HB', 'Pedir un taxi de nuevo', 'Entrar la habitación del hotel', 'Ir por el avión']

## Matrices en Python (Array multidimencional)

- Para crear un array multimecional debemos tener la sgt estructura

    ```
    ArrayNumero = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    ```

- 


## Tupla en Python

- Las tupas son inmutables, una vez creada no e puede modificar, pero si dentro de esta tenemos una lista, si podemos modificar la lista

- Para crear una tupla en Python, debemos tener la sgt estructura

    ```
    numbers = (1,2,3,4,5,6)
    print(numbers)
    ```

- Para acceder a un valor de una tupla

    ```
    numbers = (1,2,3,4,5,6)
    print(numbers[0])
    ```

## Diccionario en Python

- Son una estructura que almacenan dos datos, clave y valor. Es como un objecto de JavaScript

- Para crear un diccionario debemos tener la sgt estructura:

    ```
    config = {
        "url" : "https://www.hola.com",
        "key" : "123asdashdgasd",
        "username" : "Prueba",
        "password" : "12345",
    }
    ```

- Si queremos acceder a un valor dentro de un diccionario, ponemos la clave:

    ```
    config = {
        "url" : "https://www.hola.com",
        "key" : "123asdashdgasd",
        "username" : "Prueba",
        "password" : "12345",
    }

    #Para acceder a un valor
    print(config["url"])
    ```
    
    El valor que este va a retornar es: https://www.hola.com

- Para eliminar un elemento dentro del array, usamos del

    ```
    config = {
        "url" : "https://www.hola.com",
        "key" : "123asdashdgasd",
        "username" : "Prueba",
        "password" : "12345",
    }

    #Para eliminar un valor de un diccionario
    del config["username"]
    print(config)
    ```


- Para obtener las claves de un diccionario, usamos keys()

    ```
    config = {
        "url" : "https://www.hola.com",
        "key" : "123asdashdgasd",
        "username" : "Prueba",
        "password" : "12345",
    }

    #Obtener las claves dentro de un diccionario
    claves = config.keys()
    print(claves)
    ```
    El valor a retornar es de la clase dict_keys

- Para obtener los valores de un diccionario, usamos values()

    ```
    config = {
        "url" : "https://www.hola.com",
        "key" : "123asdashdgasd",
        "username" : "Prueba",
        "password" : "12345",
    }

    #Obtener las claves dentro de un diccionario
    claves = config.keys()
    print(claves)
    ```

    Esto nos va a retonar los valores con la clase dict_values

- Para separar los valores de un diccionario, usamos items()

    ```
    config = {
        "url" : "https://www.hola.com",
        "key" : "123asdashdgasd",
        "username" : "Prueba",
        "password" : "12345",
    }

    #Si queremos separar los valores de un diccionario
    items =  config.items()
    print(items)
    ```

    Esto nos va a retonar los valores dentro de una lista separado por tuplas

## Estructuras condicionales

- La sintaxis de un if en python es:

    ```
    x = True
    if x :
        print("Verdadero")
    ```

    Debemos tener en cuenta la identación del codigo, una vez entramos al if, debemos hacer un tab a la derecha

    Si queremos salir del if, volvemos al nivel de identación del if

- Else en Python

    ```
    x = False
    if x :
        print("Verdadero")
    else :
        print("Falso")
    ```

- Else if en Python

    ```
    x = 5

    if x > 7:
        print("Mayor")
    elif x == 5 :
        print("Es igual")
    else :
        print("Menor")
    ```
- Logica dentro de un if con operados logicos 

    - And

        ```
        x = 5

        if x > 7 and x < 10:
            print("Mayor de 7 y menor de 8")
        elif x > 4 and x < 7 :
            print("Mayor de 5 y menor de 7")
        else :
            print("No se encuentra dentro de los rangos")
        ```

    - Or

        ```
        x = 9
        y = 21

        if x > 10 or y < 20 :
            print("X es mayor de 10 o Y es menor de 20")
        else :
            print("No esta dentro del rango")
        ```

    - Not (Negación)

        ```
        is_user = True
        if not is_user :
            print("No es usuario")
        else :
            print("Es usuario")
        ```


## Funciones en Python

- type, nos dice que tipo de dato es el contenido de una variable

    ```
    print(type(nombre))
    ```
    En este caso el retorno es <class 'str'>, por lo cual str, lo inferimos como un string.
    
    Si este fuera numero nos va a retornar <class 'int'>.

- len nos permite contar la cantidad de caracteres dentro de un string
   
    ```
    nombre = "James"
    print(len(nombre))   
    ```
    En este caso nos va retorna 5, que son la cantidad de caracteres en el string.

- print 

    - La coma dentro del método print se usa para separar varios argumentos. Al hacerlo, Python añade automáticamente un espacio entre los argumentos. Esto es diferente a concatenar cadenas con el operador +, que no añade espacios adicionales.

        ```
        print("Nunca", "pares", "de", "aprender")  
        ```

        Resultado: Nunca pares de aprender

    - Uso de sep, el parámetro sep permite especificar cómo separar los elementos al imprimir. En este ejemplo, los elementos “Nunca”, “pares”, “de” y “aprender” se imprimirán con una coma y un espacio entre ellos, resultando en “Nunca, pares, de, aprender”. Puedes cambiar sep por cualquier cadena de caracteres que desees usar como separador.
  
        ```
        print("Nunca", "pares", "de", "aprender", sep=", ")
        ```

        Resultado: Nunca, pares, de, aprender


    - Uso de end, el parámetro end cambia lo que se imprime al final de la llamada a print. En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que “Nunca” y “pares” se impriman en la misma línea, resultando en “Nunca pares”. Por defecto, end es un salto de línea ("\n"), lo que hace que cada llamada a print comience en una nueva línea.
  
        ```
        print("Nunca", end=" ")
        print("pares de aprender")
        ```

        Resultado: Nunca pares de aprender

    - Impresión con formato específico, puedes controlar el formato de los números al imprimir. En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un formato específico.
  
        ```
        valor = 3.14159
        print("Valor: {:.2f}".format(valor))
        ```

        Resultado: Valor: 3.14

- input, nos permite recibir entradas del usuario, por consola
  
    ```
    nombre = input("Ingresar nombre: " )
    print(nombre)
    ```

    Resultado: El resultado ingresado

- max, nos permite obtener el numero mayor de una lista de numero
  
    ```
    numbers = [1,2,3,4,5,6,7,8,9,10]

    #Obtener el numero mayor
    print("Elemento mayor: ", max(numbers))
    ```

    Resultado: 10

- min, nos permite obtener el numero menor de una lista de numero
  
    ```
    numbers = [1,2,3,4,5,6,7,8,9,10]

    #Obtener el numero menor
    print("Elemento min: ", min(numbers))
    ```

    Resultado: 1

- del, nos permite eliminar un datos de una lista
  
    ```
    numbers = [1,2,3,4,5,6,7,8,9,10]

    #Eliminar elementos de una lista
    del numbers[0]
    print(numbers)
    ```

    Resultado: [2,3,4,5,6,7,8,9,10]

    Si no indexo un item, podemos eliminar todos los items

- id, me permite ver cual es el id que memoria de la lista

    ```
    #Para conocer el id en memoria de una lista, usamos id

    a = [1,2,3,4,5]
    b = a

    del a[0]

    print(id(a))
    print(id(b))
    ```

    En este caso de uso tanto a como b, al eliminar una posicion estos valores se registran en el mismo espacio de memoria por lo tanto lo mejor que podemos hacer un slice b = a[:] (Copia el array en un nuevo espacio de memoria)



## Metodos en Python

- lower, nos permite volver un string a minuscula

    ```
    nombre_mayus = "JAMES"
    print("JAMES a minuscula: " + nombre_mayus.lower())
    ```
    En este caso el retorno sera "james"


- upper, nos permite volver un string a mayuscula

    ```
    nombre_mayus = "james"
    print("james a mayuscula: " + nombre_minus.upper())
    ```
    En este caso el retorno sera "JAMES"


- strip, eLiminar espacio del principio y final de un string

    ```
    nombre_spaces = "       james         "
    print("Variable sin espacios: " + nombre_spaces.strip())
    ```
    En este caso el retorno será sin espacios al inicio y final, pero va a mantener los que estan dentro del primer y ultimo caracter

- append, agregar un item a una lista

    ```
    to_do = [
            "Ir al hotel",
            "Pedir un nuevo",
            "Comer HB",
            "Pedir un taxi de nuevo",
            "Entrar la habitación del hotel"
            ]

    #Agregar un item a una lista
    to_do.append("Ir por el avión")
    print(to_do)
    ```

- insert, nos permite agregar un item en una posición deseada

    ```
    to_do = [
        "Ir al hotel",
        "Pedir un nuevo",
        "Comer HB",
        "Pedir un taxi de nuevo",
        "Entrar la habitación del hotel"
        ]

    #Agregar un item en una posicion especifica
    to_do.insert(3, "Comprar regalos")
    print(to_do)
    ```
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
    ]
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
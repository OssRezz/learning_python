empleados = [
    {
        "nombre" : "James",
        "email" : "James@asd.com",
        "edad" : 28,
    },
    {
        "nombre" : "Bella",
        "email" : "Bella@asd.com",
        "edad" :  1,
    },
    {
        "nombre" : "Perro",
        "email" : "Perro@asd.com",
        "edad" :  7,
    },
    {
        "nombre" : "Perrito",
        "email" : "Perrito@asd.com",
        "edad" :  5,
    },
    {
        "nombre" : "Chloe",
        "email" : "Chloe@asd.com",
        "edad" :  2,
    },
]

#For

for empleado in empleados :
    print("Nombre: ", empleado["nombre"], "email: ",  empleado["email"], "edad: ", empleado["edad"])
    
# FOr range

for i in range(10) : 
    print(i)
    
#While
#POdemos usar break para detener la ejecución

contador = 0
while (len(empleados) - 1) > 0 and contador < len(empleados): 
    if contador == 2 :
        break
    
    contador = contador + 1
    print(empleados[contador - 1])

# Para omitir un registro y continuar con el siguiente
for i in range(10) : 
    if i == 3 :
        continue
    
    print(i)
    
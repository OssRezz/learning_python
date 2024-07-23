x = 5

if x > 7 and x < 10:
    print("Mayor de 7 y menor de 8")
elif x > 4 and x < 7 :
    print("Mayor de 5 y menor de 7")
else :
    print("No se encuentra dentro de los rangos")
    

# Or

x = 9
y = 21

if x > 10 or y < 20 :
    print("X es mayor de 10 o Y es menor de 20")
else :
    print("No esta dentro del rango")
    
#Negacion 
is_user = True
if not is_user :
    print("No es usuario")
else :
    print("Es usuario")
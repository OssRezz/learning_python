def task ():
    tasks = [
        "Ir al gym",
        "Comprar cafeeeé",
        "Ejecutar mercado",
        "Ejecutar mercadooo tenia",
    ]
    
    return tasks


with open('to_do_list.txt', 'w') as file:
    # Agregar cada tarea a una nueva línea en el archivo
    for task in task():
        file.write(f"{task}\n")    


print("Archivo to_do_list.txt creado y tareas agregadas.")

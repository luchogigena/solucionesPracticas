#Estructura de Datos
#Lista
# Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

# Crear una lista para almacenar los nombres
nombres = []

# Solicitar al usuario que ingrese 10 nombres no repetidos
while len(nombres) < 10:
    nombre = input("Ingrese un nombre: ")
    
    # Verificar si el nombre ya ha sido ingresado
    if nombre in nombres:
        print("¡Este nombre ya ha sido ingresado! Por favor, ingrese otro nombre.")
    else:
        nombres.append(nombre)

# Mostrar los nombres ingresados
print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombre)
#Estructura de Datos
#Tupla
#Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.

# Solicitar al usuario el valor de n
n = int(input("Ingrese el valor de n: "))

# Crear una lista para almacenar los números pares
numeros_pares = []

# Generar los primeros n números pares
i = 0
while len(numeros_pares) < n:
    if i % 2 == 0:
        numeros_pares.append(i)
    i += 1

# Convertir la lista de números pares a una tupla
tupla_pares = tuple(numeros_pares)

# Mostrar los datos de la tupla
print("Los primeros", n, "números pares son:", tupla_pares)

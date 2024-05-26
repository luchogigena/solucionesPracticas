#Estructura de Datos
#Diccionario
#Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

#  diccionario vacío para almacenar los datos de la persona
persona = {}

# Solicitar al usuario que ingrese los datos de la persona
persona["nombre"] = input("Ingrese el nombre de la persona: ")
persona["apellido"] = input("Ingrese el apellido de la persona: ")
persona["dni"] = input("Ingrese el DNI de la persona: ")
persona["email"] = input("Ingrese el correo electrónico de la persona: ")
persona["fecha_nacimiento"] = input("Ingrese la fecha de nacimiento de la persona (en formato dd/mm/aaaa): ")

# Mostrar los datos 
print("\nLos datos de la persona son:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
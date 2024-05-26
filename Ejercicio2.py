# Estructura Condicional:
#


# Solicitar al usuario la cantidad de unidades de leche de vaca entera
cantidad_unidades = int(input("Ingrese la cantidad de unidades que desea comprar: "))

# Calcular el costo total sin descuentos
costo_total = cantidad_unidades * 1000

# Aplicar descuentos según la cantidad de unidades compradas
if cantidad_unidades > 12 and cantidad_unidades <= 24:
    descuento = 0.1 * costo_total
elif cantidad_unidades > 24:
    descuento = 0.15 * costo_total
else:
    descuento = 0

# Aplicar descuento adicional para jubilados
es_jubilado = input("¿Es jubilado? (Sí/No): ").lower()
if es_jubilado == "sí" or es_jubilado == "si":
    descuento += 0.1 * costo_total

# Calcular el costo total final
costo_total -= descuento

# Imprimir el costo total que el cliente debe pagar
print(f"El costo total a pagar es: ${costo_total:.2f}")
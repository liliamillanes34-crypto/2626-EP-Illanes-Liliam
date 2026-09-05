# Programa para reservar asientos de una sala de cine.
# La sala tiene 3 filas y 4 columnas, representadas como una matriz.

# Crear la matriz 3x4 con todos los asientos libres (valor 0).
asientos = [[0 for _ in range(4)] for _ in range(3)]

# Solicitar la fila y la columna del asiento a reservar.
print("Ingrese la fila del asiento (0 a 2):")
fila = int(input())

print("Ingrese la columna del asiento (0 a 3):")
columna = int(input())

# Validar que la fila y la columna estén dentro del rango permitido.
if 0 <= fila < 3 and 0 <= columna < 4:
    if asientos[fila][columna] == 1:
        print("El asiento ya está reservado.")
    else:
        asientos[fila][columna] = 1
        print(f"Asiento reservado en la fila {fila}, columna {columna}.")
else:
    print("La fila o la columna ingresada está fuera del rango permitido.")

# Mostrar el estado completo de la sala utilizando bucles anidados.
print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

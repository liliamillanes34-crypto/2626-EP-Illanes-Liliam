FILAS = 5
COLUMNAS = 5

matriz = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# --- Ingreso de datos ---
print("Ingreso de valores para la matriz de 5x5")
print("-" * 40)

for fila in range(FILAS):
    for columna in range(COLUMNAS):
        valor = int(
            input(f"Ingrese el valor para la posición [{fila}][{columna}]: ")
        )
        matriz[fila][columna] = valor

# --- Presentación de resultados ---
print("\nMatriz ingresada:")
print("-" * 40)

for fila in range(FILAS):
    for columna in range(COLUMNAS):
        print(matriz[fila][columna], end="\t")
    print()

# Crear la matriz vacía (lista de listas), inicializada en cero.
# La comprensión de listas anidada genera 5 listas internas de 5 ceros,
# Una por cada fila de la matriz.
# El bucle externo (fila) recorre las 5 filas disponibles.
# El bucle interno (columna) recorre, para cada fila, las 5 columnas.
# Juntos completan las 25 posiciones de la matriz.
# Se recorre nuevamente la matriz con el mismo esquema de bucles anidados.
# end="\t" imprime los valores separados por un tabulador, en la misma línea.
# print() sin argumentos, al cerrar el bucle interno, genera el salto de
# línea que separa visualmente una fila de la siguiente.
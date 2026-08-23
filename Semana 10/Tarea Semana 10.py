# Programa con matriz de 3x3
# Autor: Liliam Illanes
# Descripción: Declara una matriz de 3x3, la recorre con ciclos e imprime sus valores

# Definir matriz como arreglo de 3x3
matriz = [[1, 3, 5]
         ,[4, 6, 8]
         ,[7, 9, 11]]

print("Valores de la matriz 3x3")
print("-" * 20)

# Recorrer la matriz con ciclos anidados
for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")

print("-" *20)
print("\nMatriz completa:")
for fila in matriz:
    print(fila)



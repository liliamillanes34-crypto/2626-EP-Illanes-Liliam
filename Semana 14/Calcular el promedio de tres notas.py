"""Programa para calcular el promedio de tres notas."""

def calcular_promedio(nota1: float, nota2: float, nota3: float)-> float:
    """Calcula el promedio de tres notas y lo devualve"""
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

if __name__ == "__main__":
    try:
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
    except EOFError:
        nota1, nota2, nota3 = 0, 0, 0

    resultado = calcular_promedio(nota1, nota2, nota3)
    print(f"El promedio de las notas es: {resultado:.2f}")



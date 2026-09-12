"""
calcular_total.py
Función que calcula el total de una compra (precio * cantidad)
"""

def calcular_total(precio, cantidad):
    """
    Calcula el total de una compra.
    precio: float o int
    cantidad: int
    retorna: float
    """
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio = 10
    cantidad = 3
    resultado = calcular_total(precio, cantidad)
    print(f"Total de la compra: {resultado}")

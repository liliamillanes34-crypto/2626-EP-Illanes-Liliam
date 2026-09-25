# Universidad Estatal Amazónica (UEA)
# Carrera: Tecnologías de la Información
# Asignatura: Fundamentos de Prgramación
# Semana 15: Colecciones de datos: Listas, conjuntos y diccionarios
# Estudiante: Liliam Illanes Burbano

# Problema de la vida real:
# Una pequeña bodega necesita registrar sus productos con la cantidad disponible,
#  conocer las categorías que maneja sin repetirlas y llevar un historial de los
#  movimientos realizados en la bodega.

# Colecciones utilizadas:
# 1. Diccionario: inventario {nombre_producto: [categoria, cantidad]}
# 2. Conjunto: categorias (evita categorías repetidas o duplicadas)
# 3. Lista: historial (guarda los movimientos en orden cronológico)

# ===============================================================================

# -------------------------------------------------------------------------------
# 1. Creación de colecciones (con datos iniciales)
# -------------------------------------------------------------------------------
inventario = {
    "arroz": ["granos", 50],
    "azúcar": ["granos", 30],
    "aceite": ["abarrotes", 20],
}

categorias = {"granos", "abarrotes"}

historial = []


# -------------------------------------------------------------------------------
# 2. Funciones del programa
# -------------------------------------------------------------------------------
def agregar_producto():
    """Inserta un producto nuevo o suma cantidad si ya existe."""
    nombre = input("Nombre del producto: "). strip(). lower()
    categoria = input("categoría: ").strip().lower()

    # Validamos que la cantidad sea un número entero positivo
    cantidad_texto = input("Cantidad: ").strip()
    if not cantidad_texto.isdigit() or int(cantidad_texto) == 0:
        print(" La cantidad debe ser un número entero mayor que cero.")
        return
    cantidad = int(cantidad_texto)

    if nombre in inventario:
        # Si el producto ya existe, solo se actualiza su cantidad
        inventario[nombre][1] += cantidad
        print(f"Se sumaron '{cantidad} unidades a '{nombre}'.")
    else:
        # Si es nuevo, se crea una nueva clave en el diccionario
        inventario[nombre] = [categoria, cantidad]
        print(f"Producto '{nombre}' agregado correctamente.")

    categorias.add(categoria)
    historial.append(f"Ingreso: {cantidad} de '{nombre}'")


def mostrar_inventario():
    """Recorre el diccionario y muestra los productos en forma de tabla."""
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    print("\n" + "-" * 45)
    print(f"{'Producto':<15} {'Categoría':<15} {'Cantidad':>10}")
    print("-" * 45)
    total_unidades = 0
    for nombre in inventario:
        categoria, cantidad = inventario[nombre]
        print(f"{nombre:<15} {categoria:<15} {cantidad:>10}")
        total_unidades += cantidad
    print("-" * 45)
    print(f"Total de productos: {len(inventario)} | Total de unidades: {total_unidades}")


def buscar_producto():
    """Busca un producto por su nombre (clave del diccionario)."""
    nombre = input("Producto a buscar: ").strip().lower()
    if nombre in inventario:
        categoria, cantidad = inventario[nombre]
        print(f"Producto: {nombre}, Categoría: {categoria}, Cantidad: {cantidad}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")


def eliminar_producto():
    """Elimina un producto del inventario usando del."""
    nombre = input("Producto a eliminar: ").strip().lower()
    if nombre in inventario:
        del inventario[nombre]
        historial.append(f"Eliminación '{nombre}")
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"No se puede eliminar '{nombre}' no existe.")


def mostrar_categorias():
    """Muestra las categorías únicas guardadas en el conjunto."""
    print("categorás registradas (sin repetir):")
    for categoria in sorted(categorias):
        print(f"- {categoria}")


def mostrar_historial():
    """Recorre la lista del historial con su número de movimiento."""
    if len(historial) == 0:
        print("No hay movimientos registrados en el historial.")
        return
    print("Historial de movimientos:")
    for posicion in range(len(historial)):
        print(f"{posicion + 1}. {historial[posicion]}")


# -------------------------------------------------------------------------------
# 3. Menú principal del programa:
# ________________________________________________________________________________
opcion = ""
while opcion != "7 ":
    print("\n===== INVENTARIO DE LA BODEGA =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Mostrar categorías")
    print("6. Mostrar historial de movimientos")
    print("7. Salir del programa")
    opcion = input("Seleccione una opción (1-7): ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        mostrar_categorias()
    elif opcion == "6":
        mostrar_historial()
    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta pronto!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-7).")

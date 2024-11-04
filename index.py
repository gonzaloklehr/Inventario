# Lista para almacenar los productos
inventario = []

# Función para agregar un producto al inventario
def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    inventario.append({"Nombre": producto, "Cantidad": cantidad, "Precio": precio})
    print(f"Producto '{producto}' agregado exitosamente.")

# Función para mostrar todos los productos en el inventario
def mostrar_productos():
    if not inventario:
        print("El inventario está vacío. Cargue un Producto.")
    else:
        print("\nInventario de Productos:")
        for i, producto in enumerate(inventario, 1):
            print(f"{i}. Nombre: {producto['Nombre']}, Cantidad: {producto['Cantidad']}, Precio: {producto['Precio']:.2f}")
        print()

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1. Agregar producto al inventario")
        print("2. Mostrar productos registrados")
        print("3. Salir")
        
        # Solicitar al usuario que seleccione una opción
        opcion = input("Selecciona una opción (1, 2 o 3): ")
        
        # Estructura de control para manejar las opciones
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("Salir del programa. ¡Chau, Hasta la próxima!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú (Para que el menú siempre se encuentre activo. Hasta que el usuario solicite Salir).
menu()

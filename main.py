from functions import *

limpiar()

def mostrar_menu():
    print("===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Eliminar libro")
    print("7. Modificar libro")
    print("8. Mostrar estadisticas")
    print("9. Salir")

opcion = 0
while opcion != 9:
    mostrar_menu()
    opcion = int(input("Seleccione una opcion: "))
    limpiar()
    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        mostrar_libros()
    elif opcion == 3:
        buscar_libro()
    elif opcion == 4:
        prestar_libro()
    elif opcion == 5:
        devolver_libro()
    elif opcion == 6:
        eliminar_libro()
    elif opcion == 7:
        modificar_libro()
    elif opcion == 8:
        mostrar_estadisticas()
    elif opcion == 9:
        print("Hasta luego.")
    else:
        print("Opcion no valida.")

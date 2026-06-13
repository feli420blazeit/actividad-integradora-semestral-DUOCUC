import os

libros = []

def limpiar():
    os.system("cls")

def agregar_libro():
    titulo = input("Ingrese el titulo del libro: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("El libro ya existe en la biblioteca.")
            return
    autor = input("Ingrese el autor del libro: ")
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "disponible": True
    }
    libros.append(nuevo_libro)
    print("Libro agregado correctamente.")

def mostrar_libros():
    if len(libros) == 0:
        print("No hay libros registrados.")
        return
    print("\nLista de libros:")
    print("-" * 40)
    for i, libro in enumerate(libros, 1):
        if libro["disponible"]:
            estado = "Disponible"
        else:
            estado = "Prestado"
        print(f"{i}. Titulo: {libro['titulo']}")
        print(f"   Autor: {libro['autor']}")
        print(f"   Estado: {estado}")
        print("-" * 40)

def buscar_libro():
    titulo = input("Ingrese el titulo a buscar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["disponible"]:
                estado = "Disponible"
            else:
                estado = "Prestado"
            print(f"Titulo: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Estado: {estado}")
            return
    print("No se encontro el libro.")

def prestar_libro():
    titulo = input("Ingrese el titulo del libro a prestar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if not libro["disponible"]:
                print("El libro ya esta prestado.")
            else:
                libro["disponible"] = False
                print("Libro prestado correctamente.")
            return
    print("No se encontro el libro.")

def devolver_libro():
    titulo = input("Ingrese el titulo del libro a devolver: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["disponible"]:
                print("El libro no estaba prestado.")
            else:
                libro["disponible"] = True
                print("Libro devuelto correctamente.")
            return
    print("No se encontro el libro.")

def eliminar_libro():
    titulo = input("Ingrese el titulo del libro a eliminar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            libros.remove(libro)
            print("Libro eliminado correctamente.")
            return
    print("No se encontro el libro.")

def modificar_libro():
    titulo = input("Ingrese el titulo del libro a modificar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("Deje en blanco para no modificar el campo.")
            nuevo_titulo = input(f"Nuevo titulo [{libro['titulo']}]: ")
            nuevo_autor = input(f"Nuevo autor [{libro['autor']}]: ")
            if nuevo_titulo != "":
                libro["titulo"] = nuevo_titulo
            if nuevo_autor != "":
                libro["autor"] = nuevo_autor
            print("Libro modificado correctamente.")
            return
    print("No se encontro el libro.")

def mostrar_estadisticas():
    total = len(libros)
    disponibles = 0
    prestados = 0
    for libro in libros:
        if libro["disponible"]:
            disponibles += 1
        else:
            prestados += 1
    print(f"Total de libros: {total}")
    print(f"Libros disponibles: {disponibles}")
    print(f"Libros prestados: {prestados}")

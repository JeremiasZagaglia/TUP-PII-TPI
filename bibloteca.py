import libro as l
#hola
# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro(lib):
    lib.append(l.nuevo_libro())
    print("\n Su libro ha sido cargado con éxito.\n Los datos almacenado son:\n\n")

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    #completar
    return None

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None

def mostrar_datos_libro(dicc):
    print(f"Código de libro: {dicc['cod']}")
    print(f"Título: {dicc['titulo']}")
    print(f"Autor: {dicc['autor']}")
    print(f"Cantidad de ejempl.prestados: {dicc['cant_ej_pr']}")
    print(f"Cantidad de ejempl.disponibles: {dicc['cant_ej_ad']}\n")
    
    
import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

# Las 5 funciones siguientes corresponden cada una con una opción del menú principal.

# Para opción 5.
def ejemplares_prestados():
    # completar
    return None

# Para opción 3.
def registrar_nuevo_libro(lib: list):
    lib.append(l.nuevo_libro())
    print("\nSu libro ha sido cargado con éxito.\nLos datos almacenado son:\n")

# Para opción 4.
def eliminar_ejemplar_libro():
    #completar
    return None

# Para opción 1.
def prestar_ejemplar_libro(lib: list):
    codigo = input("Ingrese el código del libro a buscar: ")
    dicc = buscar_libro(lib, codigo)
    if not bool(dicc): #Verificamos que haya contenido en el dicc
        print("\nNo existe ningún libro con ese código\n")
        return None
    else:
        print("Libro encontrado: \n")
        mostrar_datos_libro(dicc)
        if dicc['cant_ej_ad'] > 0:
            print("Préstamo confirmado \n")
            lib.remove(dicc) #removemos dicc con cantidad desactualizada
            dicc['cant_ej_ad'] -= 1
            dicc['cant_ej_pr'] += 1
            lib.append(dicc) #insertamos dicc con cantidad actualizada
        else:
            print("Lo sentimos, no hay ejemplares disponibles.\n")
    return None
                
# Para opción 2.
def devolver_ejemplar_libro(libros):
    codigo=input("Ingrese el codigo del libro a devolver: ")
    dicc= buscar_libro(libros, codigo)
    if dicc=={}:
        print("Error: el libro no existe")
    else:
        if dicc['cant_ej_pr']>0:
            print("Ejemplar devuelto")
            libros.remove(dicc) #removemos dicc con cantidad desactualizada
            dicc['cant_ej_pr'] -= 1
            dicc['cant_ej_ad'] += 1
            libros.append(dicc) #insertamos dicc con cantidad actualizada
        else:
            print("No existen ejemplares prestados")

    return None

"""def nuevo_libro():
    #completar
    return None"""

# Funciones auxiliares.

def mostrar_datos_libro(dicc: dict):
    print(f"Código de libro: {dicc['cod']}")
    print(f"Título: {dicc['titulo']}")
    print(f"Autor: {dicc['autor']}")
    print(f"Cantidad de ejempl.disponibles: {dicc['cant_ej_ad']}\n")
    
def buscar_libro(lib: list, cod: str) -> dict:
    dicc = {}
    for elemento in lib:
        dicc.update(elemento)
        if dicc['cod'] == cod:
            return dicc
        dicc = {} 
    return dicc #si el código no coincide se retorna un diccionario vacío.
# Crear un diccionario para cada libro

import cod_generator as cg

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    cant_ejempl = int(input("Ingrese la cantidad de ejemplares del nuevo libro: "))
    titulo = input("Ingrese el título del nuevo libro: ")
    autor = input("Ingrese el autor del nuevo libro: ")
    libro_n = {'cod': generar_codigo(), 'cant_ej_ad': cant_ejempl, 'cant_ej_pr': 0, "titulo": titulo, "autor": autor}
    return libro_n

def generar_codigo():
    
    return cg.generar()
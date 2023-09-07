# Trabajo Práctico I - Programación II


import os
import bibloteca as bib

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            #completar
            print()
        elif int(opt) == 2:
            #completar
            print()
        elif int(opt) == 3:
            bib.registrar_nuevo_libro(bib.libros)
            bib.mostrar_datos_libro(bib.libros[-1])
        elif int(opt) == 4:
            #completar
            print()
        elif int(opt) == 5:
            #completar
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa
    os.system ("cls") #Limpiar pantalla

print("Hasta luego!.")
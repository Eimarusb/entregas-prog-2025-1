#!/usr/bin/env python3

"""
Título de práctica: Transformaciones de texto

Descripción extendida del programa:
Este programa permite al usuario aplicar diferentes transformaciones a un texto,
como cambiar a mayúsculas, minúsculas, capitalización, etc., mediante un menú interactivo.

Autor: EimarEsteban Garcia Ramirez <eegarciar@academia.usbbog.edu.co>
Fecha: 2025-05-04
"""

# No se requieren módulos adicionales para este programa
def run():
    """script entrypoint"""

    while True:  
        # Menu de opciones
        print("a. Para pasar a minúsculas (abcde)")
        print("b. Para pasar a mayúsculas (ABCDE)")
        print("c. Para invertir mayúsculas y minúsculas (AbCdE)")
        print("d. Para pasar a capitalización (Hola como estas)")
        print("e. Para pasar a titulación (Hola Como Esta)")
        print("f. Para reemplazar espacios por guiones bajos (_)")
        print("g. Para salir.")

        # Solicita al usuario que seleccione una opción
        seleccionDeUsuario = input("Ingresa la modificación que le quieres hacer a tu texto: ")

        if seleccionDeUsuario == 'g':  # Opción para salir del programa
            print("Saliendo... ¡Hasta luego!")
            break 

        # Verifica si la opción ingresada es válida
        if seleccionDeUsuario not in ('a', 'b', 'c', 'd', 'e', 'f'):
            print("Opción inválida. Intente nuevamente.")
            continue 

        # Solicita al usuario que ingrese el texto a modificar
        textodeprueba = input("Ingresa un texto para modificar: ")

        # Aplica la transformación según la opción seleccionada
        if seleccionDeUsuario == 'a':
            # Convierte todo el texto a minúsculas
            print("Tu nuevo texto en minúsculas es:", textodeprueba.lower())
        elif seleccionDeUsuario == 'b':
            # Convierte todo el texto a mayúsculas
            print("Tu nuevo texto en mayúsculas es:", textodeprueba.upper())
        elif seleccionDeUsuario == 'c':
            # Invierte mayúsculas por minúsculas y viceversa
            print("Tu nuevo texto con mayúsculas y minúsculas invertidas es:", textodeprueba.swapcase())
        elif seleccionDeUsuario == 'd':
            # Capitaliza solo la primera letra del texto
            print("Tu nuevo texto capitalizado es:", textodeprueba.capitalize())
        elif seleccionDeUsuario == 'e':
            # Pone la primera letra de cada palabra en mayúscula (título)
            print("Tu nuevo texto en formato de título es:", textodeprueba.title())
        elif seleccionDeUsuario == 'f':
            # Reemplaza los espacios por guiones bajos
            print("Tu texto con espacios reemplazados por _ es:", textodeprueba.replace(" ", "_"))


# Condicional que verifica si el archivo se está ejecutando directamente
if __name__ == "__main__":
    run()  # Llama a la función principal para iniciar el programa

#!/usr/bin/env python3

"""
Título de práctica: Calculadora de operaciones básicas

Descripción:
Este programa permite al usuario realizar operaciones matemáticas básicas:
suma, resta, multiplicación, división, potenciación, división entera y módulo.
El usuario puede cancelar una operación escribiendo 'x'.

Autor: TuNombre <tu@correo.com>
Fecha: 2025-04-10
"""

# Función para verificar si el valor ingresado es un número válido
def es_numero(valor):
    """Verifica si el valor ingresado es un número válido."""
    if valor.lower() == 'x':
        return True  # Permitir cancelar la operación
    if valor.replace('.', '', 1).isdigit():  # Permite flotantes como 3.14
        return True
    if valor.lstrip('-').isdigit():  # Permite enteros negativos como -5
        return True
    return False


def run():
    """Punto de entrada principal del programa"""

    while True:
        print("\nEscoge una operación básica:")
        print("a. Suma (+)")
        print("b. Resta (-)")
        print("c. Multiplicación (*)")
        print("d. División (/)")
        print("e. Potenciación (^)")
        print("f. División entera (//)")
        print("g. Módulo (%)")
        print("h. Salir")

        seleccionDeUsuario = input("Ingrese la letra de la operación que desea realizar (a-h): ").lower()

        if seleccionDeUsuario == 'h':
            print("Saliendo... ¡Hasta luego!")
            break  # Finaliza el programa

        if seleccionDeUsuario not in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
            print("Opción inválida. Intente nuevamente.")
            continue

        # Algunas operaciones requieren enteros (como división entera o módulo)
        requiere_enteros = seleccionDeUsuario in ('f', 'g')

        # Solicita el primer número
        while True:
            primerTermino = input("Escriba un número (o 'x' para cancelar): ")
            if primerTermino.lower() == 'x':
                print("Operación cancelada.")
                break
            if es_numero(primerTermino):
                primerTermino = int(primerTermino) if requiere_enteros else float(primerTermino)
                break
            print("Entrada no válida. Intente nuevamente.")

        if primerTermino == 'x':
            continue

        # Solicita el segundo número
        while True:
            segundoTermino = input("Escriba otro número (o 'x' para cancelar): ")
            if segundoTermino.lower() == 'x':
                print("Operación cancelada.")
                break
            if es_numero(segundoTermino):
                segundoTermino = int(segundoTermino) if requiere_enteros else float(segundoTermino)
                break
            print("Entrada no válida. Intente nuevamente.")

        if segundoTermino == 'x':
            continue

        # Ejecuta la operación seleccionada
        if seleccionDeUsuario == 'a':
            resultado = primerTermino + segundoTermino
            print(f"La suma de {primerTermino} y {segundoTermino} es {resultado}")
        elif seleccionDeUsuario == 'b':
            resultado = primerTermino - segundoTermino
            print(f"La resta de {primerTermino} y {segundoTermino} es {resultado}")
        elif seleccionDeUsuario == 'c':
            resultado = primerTermino * segundoTermino
            print(f"La multiplicación de {primerTermino} y {segundoTermino} es {resultado}")
        elif seleccionDeUsuario == 'd':
            if segundoTermino != 0:
                resultado = primerTermino / segundoTermino
                print(f"La división de {primerTermino} entre {segundoTermino} es {resultado}")
            else:
                print("Error: Nunca dividas por cero.")
        elif seleccionDeUsuario == 'e':
            resultado = primerTermino ** segundoTermino
            print(f"{primerTermino} elevado a la {segundoTermino} es {resultado}")
        elif seleccionDeUsuario == 'f':
            if segundoTermino != 0:
                resultado = primerTermino // segundoTermino
                print(f"La división entera de {primerTermino} entre {segundoTermino} es {resultado}")
            else:
                print("Error: Nunca dividas por cero.")
        elif seleccionDeUsuario == 'g':
            if segundoTermino != 0:
                resultado = primerTermino % segundoTermino
                print(f"El módulo de {primerTermino} entre {segundoTermino} es {resultado}")
            else:
                print("Error: Nunca dividas por cero.")

        # Pregunta si se desea realizar otra operación
        continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("Saliendo... ¡Hasta luego!")
            break


# Punto de entrada del script cuando se ejecuta directamente
if __name__ == "__main__":
    run()

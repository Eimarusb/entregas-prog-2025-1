#!/usr/bin/env python3

"""
Calculadora1: Prototipo

Descripción extendida del programa

Autor: Eimar Esteban Garcia Ramirez <eegarciar@academia.usbbog.edu.co>/<eimarg522@gmail.com>
Fecha: 2025-03-013
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""
    print("Escoge una operacion basica :):")  
    print("1. Suma +")
    print("2. Resta -")
    print("3. Multiplicación *")
    print("4. División ")
    seleccionDeUsuario = input("Ingrese el número de la operación que desea realizar (1-4): ")
    primerTermino = int(input("Escriba un número entero: "))
    segundoTermino = int(input("Escriba otro número entero: "))
    if seleccionDeUsuario == '1':
        resultado = primerTermino + segundoTermino
        print(f"La suma de {primerTermino} y {segundoTermino} es {resultado}")
    elif seleccionDeUsuario == '2':
        resultado = primerTermino - segundoTermino
        print(f"La resta de {primerTermino} y {segundoTermino} es {resultado}")
    elif seleccionDeUsuario == '3':
        resultado = primerTermino * segundoTermino
        print(f"La multiplicación de {primerTermino} y {segundoTermino} es {resultado}")
    elif seleccionDeUsuario == '4':
        if segundoTermino != 0:
            resultado = primerTermino / segundoTermino
            print(f"La división de {primerTermino} entre {segundoTermino} es {resultado}")
        else:
            print("Nunca dividas por cero 0")
 
    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()

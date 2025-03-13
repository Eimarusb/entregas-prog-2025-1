#!/usr/bin/env python3

"""
Calculadora1: Prototipo

Descripción extendida del programa

Autor: Eimar Esteban Garcia Ramirez <eegarciar@academia.usbbog.edu.co>/<eimarg522@gmail.com>
Fecha: 2025-03-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí
# Menú de selección de operación
print("Escoge una operacion basica :):")
print("1. Suma +")
print("2. Resta -")
print("3. Multiplicación *")
print("4. División /")

# Seleccción de operaciones
selecciónDeUsuario = input("Ingrese el número de la operación que desea realizar (1-4): ")

# Solicitar operandos solo si se va a realizar una operación
primerTermino = int(input("Escriba un número entero: "))
segundoTermino = int(input("Escriba otro número entero: "))

# Ejecutar suma
if selecciónDeUsuario  == '1':
    resultado = primerTermino + segundoTermino
    print(f"La suma de {primerTermino} y {segundoTermino} es {resultado}")
# Ejecutar resta
elif selecciónDeUsuario  == '2':
    resultado = primerTermino - segundoTermino
    print(f"La resta de {primerTermino} y {segundoTermino} es {resultado}")
# Ejecutar multiplicacion
elif selecciónDeUsuario == '3':
    resultado = primerTermino * segundoTermino
    print(f"La multiplicación de {primerTermino} y {segundoTermino} es {resultado}")
# Ejecutar division
elif selecciónDeUsuario == '4':
    if segundoTermino != 0:  #signo ! significa distinto a...
        resultado = primerTermino / segundoTermino
        print(f"La división de {primerTermino} entre {segundoTermino} es {resultado}")
    else:
        print("Nunca dividas por cero 0")
#si no se escoge opcion de 1-4, ejecutar de nuevo el codigo 
else:
    print("selecciona opciones 1/2/3/4.")


    # Saludo
    print("Hola mundo!")

    # **** ****


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()

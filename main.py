import os
import platform

from laboratorio_poo import (
    ColaboradorTiempoCompleto,
    ColaboradorTiempoParcial,
    GestionColaboradores,
)

def limpiar_pantalla():
    '''Limpiar la pantalla según el sistema operativo'''
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("=======MENU DE COLABORADORES========")
    print("1. Agregar Colaborador Tiempo Completo")
    print("2. Agregar Colaborador Tiempo Parcial")
    print("3. Buscar Colaborador por DNI")
    print("4. Actualizar Colaborador por DNI")
    print("5. Eliminar colaborador por DNI")
    print("6. Mostrar todos los colaboradores")
    print("7. Salir")
    print("==================================")


def agregar_colaborador(gestion,tipo_colaborador):
    try:
        dni = int(input("Ingrese DNI del colaborador: "))
        nombre = input("Ingrese Nombre del colaborador: ")        
        apellido = input("Ingrese Apellido del colaborador: ")
        edad = int(input("Ingrese la edad del colaborador: "))
        salario = float(input("Ingrese el salario del colaborador: "))
        #departamento = input("Ingrese el departamento del colaborador: ")

        #colaborador = ColaboradorTiempoCompleto(dni, nombre, apellido, edad, salario, departamento)

        if tipo_colaborador == "1":
            departamento = input("Ingrese el departamento del colaborador: ")
            colaborador = ColaboradorTiempoCompleto(dni, nombre, apellido, edad, salario, departamento)
        elif tipo_colaborador == "2":
            horas_semanales = float(input("Ingrese las horas semanales del colaborador: "))
            colaborador = ColaboradorTiempoParcial(dni, nombre, apellido, edad, salario, horas_semanales)
        else:
            print("Tipo de colaborador no válido")
            return

        gestion.crear_colaborador(colaborador)
        input("Presione enter para continuar")

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_colaborador_por_dni(gestion):
    dni = input("Ingrese el DNI: ")
    #gestion.leer_colaborador(dni)
    colaborador = gestion.leer_colaborador(dni)
    if colaborador:
        print(f"Colaborador encontrado: {colaborador}")
    else:
        print("Colaborador no encontrado.")
    input('Presione enter para continuar...')

def actualizar_salario_colaborador(gestion):
    dni = input("Ingrese el DNI del colaborador a actualizar salario: ")
    salario = float(input("Ingrese el salario actualizado del colaborador: "))
    gestion.actualizar_colaborador(dni, salario)
    input("Presione enter para continuar...")

def eliminar_colaborador_por_dni(gestion):
    dni = input("Ingrese el DNI del colaborador que se desea eliminar: ")
    gestion.eliminar_colaborador(dni)
    input("Presione enter para continuar...")

def mostrar_todos_los_colaboradores(gestion):
    print("LISTADO COMPLETO DE COLABORADORES")
    for colaborador in gestion.leer_datos().values():
        if 'departamento' in colaborador:
            print(f"{colaborador['nombre']} - Departamento {colaborador['departamento']} - Salario ${colaborador['salario']}")
        else:
            print(f"{colaborador['nombre']}- Horas semanales {colaborador['horas_semanales']} - Salario ${colaborador['salario']}")
    print("======================================")
    input("Presione enter para continuar...")

def main():
    archivo = "colaboradores.json"
    gestion = GestionColaboradores(archivo)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_colaborador(gestion, "1")
        elif opcion == "2":
            agregar_colaborador(gestion, "2")

        if opcion == "3":
            buscar_colaborador_por_dni(gestion)

        elif opcion == "4":
            actualizar_salario_colaborador(gestion)

        elif opcion == "5":
            eliminar_colaborador_por_dni(gestion)     

        elif opcion == "6":
            mostrar_todos_los_colaboradores(gestion)    

        elif opcion == "7":
            print("Salir del menú")
            break
        else:
            print("opción no valida, seleccione la opción correcta (1 al 7)")
            input("Presione enter para continuar")

if __name__ == "__main__":
    main()
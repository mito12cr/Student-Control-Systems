#    Jaime Vanegas Villalobos
#    13/05/2026
#    Python Student-Control-Systems
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Actions.Students_Actions import (Add_New_Student,Delete_student,Search_student_Grades,Top_3_Average,View_All_students)


def display_menu():
    print("\n=============================================")
    print("        Sistema de Control de Estudiantes             ")
    print("=============================================\n")


    print("1. Para Agregar un Estudiante")
    print("2. Para Eliminar un Estudiante")
    print("3. Para Consultar Notas de un Estudiante")
    print("4. Para Ver los Mejores 3 Promedios de Estudiantes")
    print("5. Para Ver Todos los Estudiantes") # <-- Agregada opción 5
    print("6. Para SALIR")

def menu_run():
    while True:
        display_menu()

        opcion = input("\nSeleccione una opcion del 1 - 6: ")

        if opcion == "1":
            Add_New_Student()
        elif opcion == "2":
            Delete_student()
        elif opcion == "3" :
            Search_student_Grades()
        elif opcion == "4":
            Top_3_Average()
        elif opcion == "5":
            View_All_students()
        elif opcion =="6":
            print("\n Hasta la Próxima!!")
            break                    
        else:
            print("\n Opción no válida. Por favor, elija un número del 1 al 6.")


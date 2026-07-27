#    Jaime Vanegas Villalobos
#    13/05/2026
#    Python Student-Control-Systems
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Actions.Students_Actions import (Add_New_Student,Delete_student,Search_student_Grades,Top_3_Average,View_All_students,Load_From_CSV,Save_To_CSV,General_Average)


def display_menu():
    print("\n=============================================")
    print("        Sistema de Control de Estudiantes             ")
    print("=============================================\n")

    print("1. Para Agregar un Estudiante a la Memoria")
    print("2. Para Eliminar un Estudiante de la Memoria")
    print("3. Para Consultar Notas (En Memoria)")
    print("4. Para Ver los Mejores 3 Promedios (En Memoria)")
    print("5. Para Ver el PROMEDIO GENERAL del Sistema") # <-- Nueva opción 5
    print("6. Para Ver Todos los Estudiantes (En Memoria)")
    print("7. IMPORTAR Datos desde el Archivo CSV")
    print("8. EXPORTAR / GUARDAR Cambios al Archivo CSV")
    print("9. Para SALIR")

def menu_run(session_students):
    while True:
        display_menu()

        option = input("\nSeleccione una option del 1 - 9: ")

        if option == "1":
            Add_New_Student(session_students)
        elif option == "2":
            Delete_student(session_students)
        elif option == "3":
            Search_student_Grades(session_students)
        elif option == "4":
            Top_3_Average(session_students)
        elif option == "5":
            General_Average(session_students) # <-- Llamamos a la nueva función
        elif option == "6":
            View_All_students(session_students)
        elif option == "7":
            Load_From_CSV(session_students)
        elif option == "8":
            Save_To_CSV(session_students)
        elif option == "9":      
            print("\n ¡Hasta la Próxima!!")
            break                    
        else:
            print("\n Opción no válida. Por favor, elija un número del 1 al 9.")


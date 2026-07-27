#    Jaime Vanegas Villalobos
#    13/05/2026
#    Python Student-Control-Systems
import os
import csv

FIELDNAMES = ["Nombre","Apellido","Seccion","N_Español","N_Ingles","N_Sociales","N_Ciencias"]

def export_students_to_csv(student_list):
    try:
        existing_file = os.path.exists('Students.csv')
        with open('Students.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames=FIELDNAMES)
            if not existing_file:
                writer.writeheader()
            writer.writerows(student_list)
        print("\nLos Datos han sido Exportado con Éxito al archivo CSV !! ")

    except Exception as e:
        print(f"Error al intentar Exportar los datos: {e}")

def import_students_from_csv():
    if not os.path.exists('Students.csv'):
        return []
    try:
        with open("Students.csv", 'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list (reader)
    except Exception as e:
        print(f"Error al intentar Importar los datos: {e}")
        return []      

def rewrite_all_students_to_csv(student_list):
    try:
        with open('Students.csv', 'w', newline='', encoding='utf-8')as file:
            writer = csv.DictWriter(file,fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(student_list)

    except Exception as e:
        print(f"Ha Ocurrido un Error al Actualizar el Archivo: {e}")                          
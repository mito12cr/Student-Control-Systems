#    Jaime Vanegas Villalobos
#    13/05/2026
#    Python Student-Control-Systems

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data.Data_Students import export_students_to_csv, import_students_from_csv, rewrite_all_students_to_csv

def request_valid_text(field_name):
    while True:
        valor = input(f"{field_name}").strip()
        if valor:
            return valor
        print(f"ERROR: El Campo '{field_name}' No puede quedar vacío!! ")


def request_valid_note(school_subject):
    while True:
        try:
            entrada = input(f"Nota de: {school_subject} (0-100): ").strip()
            note = float(entrada)

            if 0 <= note <= 100:
                return entrada
            else:
                print("Error: La Nota debe estar en un rango de entre 0 y 100")

        except ValueError:
            print("Error: Debe Digitar un Número Válido (Ej: 70 - 90).")      
            
def Add_New_Student():   # FUNCION PARA AGREGAR UN NUEVO ESTUDIANTE
    
    new_student = []  

    print("\n ----- Registro de Estudiantes -----")
    while True:
        nombre     = request_valid_text("\nNombre: ")
        apellido   = request_valid_text("\nApellido: ")
        seccion    = request_valid_text("\nSección: ")

        print("\n--- Ingrese las Calificaciones ---")
        n_español  = request_valid_note("Español")
        n_ingles   = request_valid_note("Ingles")
        n_sociales = request_valid_note("Sociales")
        n_ciencias = request_valid_note("Ciencias")
        
        new_student.append([nombre,apellido,seccion,n_español,n_ingles,n_sociales,n_ciencias])

        opcion = input("Desea Guardar otro Estudiante?  s/n: ").lower()

        if opcion != 's':
                break
    export_students_to_csv(new_student)


def Delete_student():       # FUNCION PARA ELIMINAR UN ESTUDIANTE
    print("\n=============================================")
    print("             Eliminar un Estudiante          ")
    print("=============================================\n")

    students = import_students_from_csv()

    if not students:
        print("No hay Estudiantes registrados o el que deseas buscar no Existe!!")
        return
    
    student_to_delete = request_valid_text("Ingrese el nombre del Estudiante que desea Eliminar: ").strip()

    keep_students = []
    found_to_delete = False

    for row in students:
        if len(row) == 7:
            if row[0].strip().lower() == student_to_delete.lower():
                found_to_delete = True
                print(f"Estudiante Encontrado y Eliminado: {row[0]} {row[1]} de la Sección: {row[2]}")
            else:
                keep_students.append(row)

    if found_to_delete:
        confirmation_to_delete = input("\n Está seguro que desea aplicar los cambios? s/n: ").lower()
        if confirmation_to_delete == 's':
            rewrite_all_students_to_csv(keep_students)
            print("El Archivo CSV se ha Actualizado con Exito!!")
        else:
            print("No Se Realizaron los cambios!!!")

    else:
        print(f"No se ha encontrado ningún estudiante con el nombre de: {student_to_delete}")


def Search_student_Grades():    # FUNCION PARA BUSCAR POR NOMBRE A UN ESTUDIANTE
    print("\n=============================================")
    print("           Buscar Notas de Estudiante        ")
    print("=============================================\n")

    students = import_students_from_csv()

    if not students:
        print("No hay Estudiantes registrados o el que deseas buscar no Existe!!")
        return
    
    student_to_search = input("Ingrese el Nombre del Estudiante que deseas encontrar y revisar sus Notas: ").strip()

    find_students = []

    for row in students:
        if len(row) == 7:
            if row[0].strip().lower() == student_to_search.lower():
                find_students.append(row)

    if not find_students:
        print(f"No se Encontraron Estudiantes con el nombre de: {student_to_search}")    
    else:
        plural = "s" if len(find_students) > 1 else ""
        print(f"\n Se encontró {len(find_students)} estudiante{plural}:")
        print("-" * 80)
        print(f"{'Nombre':<12} {'Apellido':<12} {'Sección':<8} {'Español':<10} {'Inglés':<10} {'Sociales':<10} {'Ciencias':<10}")
        print("-" * 80)        

        for row in find_students:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<8} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]:<10}")
            
        print("-" * 80)      

def Top_3_Average():    # FUNCION PARA MOSTRAR LOS 3 MEJORES PROMEDIOS DE TODOS LOS ESTUDIANTES
    print("\n=============================================")
    print("        Top 3 Mejores Promedios de Alumnos    ")
    print("=============================================\n")

    students = import_students_from_csv()

    if not students:
        print("No hay Estudiantes Registrados para Calcular los Promedios!!")
        return
    
    grades_list = []

    for row in students:
        if len(row) == 7:
            try:
                notes = [float(row[i]) for i in range(3,7)]
                average = sum(notes) / 4

                name = f"{row[0]} {row[1]}"
                grades_list.append([name, row[2], round(average, 2)])

            except ValueError:
                continue   
            
    if not grades_list:
        print(" No se pudieron Calcular los promedios, verifique que las notas sean Números!!")
        return

    grades_list.sort(key=lambda x: x[2], reverse=True)    # En esta linea con el metodo 'sort()' se ordenará la nueva lista 'grades_list' apuntando a la posicion[2] de esa lista que sería el promedio 'average'
                                                        # y gracias al reverse=true lo ordena de mayor a menor ya que originalmente los acomoda de menor a mayor.      
    
    top_3 = grades_list[:3]  # acá se guardaran solo los primeros 3 registros de la nueva lista gracias al simbolo '[:3]' ya que esto hace un 'slicing' a partir del indice indicado en mi caso el [3]

    print(f"{'Puesto': <8} {'Estudiante': <25} {'Seccion': <10} {'Promedio': <10}")
    print("-" * 50)

    for indice,alumno in enumerate(top_3, start=1):
        print(f"#{indice:<7} {alumno[0]:<25} {alumno[1]:<10} {alumno[2]:<10}")

    print("-" * 55)  


def View_All_students():
    print("=============================================")
    print(" ----- Total de Estudiantes -----")
    print("=============================================")

    students = import_students_from_csv()

    if not students:
        print("No se encuentrar Estudiantes Registrados Actualmente en el Sistema Aún!!")
        return
    
    print(f"{'Nombre':<12} {'Apellido':<12} {'Sección':<8} {'Español':<10} {'Inglés':<10} {'Sociales':<10} {'Ciencias':<10}")
    print("-" * 80)

    for row in students:
        if len(row) == 7:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<8} {row[3]:<10} {row[4]:<10} {row[5]:<10} {row[6]:<10}")

    print("-" * 80)
    print(f"El total de estudiantes: {len(students)}")                 


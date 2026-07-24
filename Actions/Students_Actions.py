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
            
def Add_New_Student(student_list):   # FUNCION PARA AGREGAR UN NUEVO ESTUDIANTE JUNTO CON LA LISTA EN MEMORIA
    
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
        
        student_list.append({
                            "Nombre":    nombre,
                            "Apellido":  apellido,
                            "Seccion":   seccion,
                            "N_Español": n_español,
                            "N_Ingles":  n_ingles,
                            "N_Sociales":n_sociales,
                            "N_Ciencias":n_ciencias
                            })

        opcion = input("Desea Guardar otro Estudiante?  s/n: ").lower()

        if opcion != 's':
                break

def Delete_student(student_list):       # FUNCION PARA ELIMINAR UN ESTUDIANTE JUNTO CON LA LISTA EN MEMORIA
    print("\n=============================================")
    print("             Eliminar un Estudiante          ")
    print("=============================================\n")

    if not student_list:
        print("No hay Estudiantes cargados en la memoria actual !!")
        return
    
    student_to_delete = request_valid_text("Ingrese el nombre del Estudiante que desea Eliminar de la Memoria: ").strip()
    found_to_delete = False

    for row in student_list:
        if 'Nombre' in row and row["Nombre"].strip().lower() == student_to_delete.lower():
            student_list.remove(row)
            found_to_delete = True
            print(f" Estudiante {row['Nombre']} removido de la memoria con éxito.")
            break

    if not found_to_delete:
        print(f" No se ha encontrado ningún estudiante en memoria con el nombre de: {student_to_delete}")


def Search_student_Grades(student_list):    # FUNCION PARA BUSCAR POR NOMBRE A UN ESTUDIANTE MEDIANTE LA LISTA EN MEMORIA
    print("\n=============================================")
    print("           Buscar Notas de Estudiante        ")
    print("=============================================\n")

    if not student_list:
        print("No hay Estudiantes cargados en la memoria Actual !!")
        return
    
    student_to_search = input("Ingrese el Nombre del Estudiante que deseas encontrar y revisar sus Notas: ").strip()
    find_students = [row for row in student_list if "Nombre" in row and row["Nombre"].strip().lower() == student_to_search.lower()]

    if not find_students:
        print(f"No se Encontraron Estudiantes en la memoria con el nombre de: {student_to_search}")    
    else:
        plural = "s" if len(find_students) > 1 else ""
        print(f"\n Se encontró {len(find_students)} estudiante{plural} en memoria:")
        print("-" * 80)
        print(f"{'Nombre':<12} {'Apellido':<12} {'Sección':<8} {'Español':<10} {'Inglés':<10} {'Sociales':<10} {'Ciencias':<10}")
        print("-" * 80)        

        for row in find_students:
            print(f"{row['Nombre']:<12} {row['Apellido']:<12} {row['Seccion']:<8} {row['N_Español']:<10} {row['N_Ingles']:<10} {row['N_Sociales']:<10} {row['N_Ciencias']:<10}")
            
        print("-" * 80)      

def Top_3_Average(student_list):    # FUNCION PARA MOSTRAR LOS 3 MEJORES PROMEDIOS DE TODOS LOS ESTUDIANTES
    print("\n=============================================")
    print("        Top 3 Mejores Promedios de Alumnos    ")
    print("=============================================\n")

    if not student_list:
        print("No hay Estudiantes Cargados en la Memoria para Calcular los Promedios!!")
        return
    
    grades_list = []

    for row in student_list:
        if "Nombre" in row:
            try:
                notes = [
                    float(row['N_Español']),
                    float(row['N_Ingles']),
                    float(row['N_Sociales']),
                    float(row['N_Ciencias'])
                ]
                average = sum(notes) / 4

                name = f"{row["Nombre"]} {row["Apellido"]}"
                grades_list.append([name, row["Seccion"], round(average, 2)])

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


def View_All_students(student_list):
    print("=============================================")
    print(" ----- Total de Estudiantes -----")
    print("=============================================")

    if not student_list:
        print("La Memoria está vacía, debes registrar estudiantes o importar el csv!!")
        return
    
    print(f"{'Nombre':<12} {'Apellido':<12} {'Sección':<8} {'Español':<10} {'Inglés':<10} {'Sociales':<10} {'Ciencias':<10}")
    print("-" * 80)

    for row in student_list:
        if "Nombre" in row:
            print(f"{row['Nombre']:<12} {row['Apellido']:<12} {row['Seccion']:<8} {row['N_Español']:<10} {row['N_Ingles']:<10} {row['N_Sociales']:<10} {row['N_Ciencias']:<10}")

    print("-" * 80)
    print(f"El total de estudiantes en Sessión: {len(student_list)}")         

def Load_From_CSV(student_list):
    print("\nCargando Datos Desde Students.csv...")
    csv_data = import_students_from_csv()
    if csv_data:
        student_list.clear()
        student_list.extend(csv_data)
        print(f"Se importaron {len(csv_data)} estudiantes a la sesión de memoria !!")
    else:
        print("El Archivo CSV está vacío o No Existe en el contexto Actual !!")

def Save_To_CSV(student_list):
    if not student_list:
        print("La Memoria está vacía. No hay datos que exportar !!")
        return
    print("\nGuardando cambios en el archivo Students.csv...")
    rewrite_all_students_to_csv(student_list)
    print("Todo el contenido de la memoria ha sido guardado con éxito!")

def General_Average(student_list):  # Mi funcion de calculo general por estudiante
    print("\n=============================================")
    print("          Promedio General del Sistema       ")
    print("=============================================\n")

    if not student_list:
        print("No hay Estudiantes cargados en la memoria para calcular el promedio general.")
        return
    
    sum_of_averages = 0  
    total_valids = 0

    for row in student_list:
        if "Nombre" in row:
            try:
                notes = [
                    float(row['N_Español']),
                    float(row['N_Ingles']),
                    float(row['N_Sociales']),
                    float(row['N_Ciencias'])
                ]
                individual_average = sum(notes) / 4
                sum_of_averages += individual_average
                total_valids += 1
            
            except ValueError:
                continue

    if total_valids == 0:
        print("No se encontraron calificaciones numéricas válidas para promediar.")
    else:
        global_average = sum_of_averages / total_valids
        print(f"Estadísticas Globales del Sistema:")
        print("-" * 50)
        print(f" Total de alumnos evaluados: {total_valids}")
        print(f" Promedio general institucional: {round(global_average, 2)}")
        print("-" * 50)

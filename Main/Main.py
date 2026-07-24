#    Jaime Vanegas Villalobos
#    13/06/2026
#    Python Student-Control-Systems

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Menu.Menu_Student import menu_run

if __name__ == "__main__":  
    sesion_student_list = []   # Creo la lista que estará en memoria para ser utilizada por el sistema
    menu_run(sesion_student_list) # De esta manera la inyectamos al menú del sistema 
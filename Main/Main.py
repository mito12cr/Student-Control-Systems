#    Jaime Vanegas Villalobos
#    13/06/2026
#    Python Student-Control-Systems

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Menu.Menu_Student import menu_run

if __name__ == "__main__":  
    menu_run()
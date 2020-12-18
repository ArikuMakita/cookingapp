from utils.clear_terminal import clear_terminal
from menus.main_menu.main_menu import main_menu

def init_menus():
    clear_terminal()
    work = True
    while work:
        main_menu()
from menus.find_menu.find_menu import find_menu
from menus.create_menu.create_menu import create_menu
from menus.view_category_menu.view_category_menu import view_category_menu
from menus.quit_from_app.quit_from_app import quit_from_app

MAIN_MENU_ANSWERS = {
    'Найти': find_menu,
    'Создать': create_menu,
    'Просмотреть': view_category_menu,
    'Выйти': quit_from_app,
}
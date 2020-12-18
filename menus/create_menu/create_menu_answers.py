from utils.back import back
from menus.create_dish_menu.create_dish_menu import create_dish_menu
from menus.create_category_menu.create_category_menu import create_category_menu

CREATE_MENU_ANSWERS = {
    'Назад': back,
    'Новое блюдо': create_dish_menu,
    'Новая категория': create_category_menu,
}
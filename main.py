from core.init_database import init_database
import regex
from pprint import pprint
from PyInquirer import prompt
from utils.get_elem_choices_and_title_to_id import get_elem_choices_and_title_to_id
from utils.back import back
from services.DishService import (
    get_all_dish,
    create_dish,
    get_dish_by_category_id,
    get_dish_by_id
)
from services.CategoryService import get_all_category, create_category
from validators import NumberValidator, RequiredValidator
from menus.return_menu.return_menu import return_menu
from utils.clear_terminal import clear_terminal
from menus.create_dish_menu.create_dish_menu import create_dish_menu
from menus.create_menu.create_menu import create_menu
from menus.create_category_menu.create_category_menu import create_category_menu
from menus.quit_from_app.quit_from_app import quit_from_app


def find_menu():
    print('Меню поиска')


def view_category_menu():

    categories = get_all_category()
    if not len(categories):
        return return_menu('Создайте категорию')

    category_choices, category_title_to_id = get_elem_choices_and_title_to_id(
        categories)

    view_category_questions = [{
        'type': 'list',
        'name': 'category',
        'message': 'Выберите категорию: ',
        'choices': category_choices,
    }]
    answer = prompt(view_category_questions)
    selected_category = answer['category']
    selected_category_id = category_title_to_id[selected_category]

    # TODO: Вынести в отдельную функцию view_dish_menu
    dishes = get_dish_by_category_id(selected_category_id)
    if not len(dishes):
        return return_menu('Создайте блюда')

    view_dish_choices, dish_title_to_id = get_elem_choices_and_title_to_id(
        dishes)

    view_dish_questions = [{
        'type': 'list',
        'name': 'dish',
        'message': 'Выберите блюдо: ',
        'choices': view_dish_choices,
    }]
    answer = prompt(view_dish_questions)
    selected_dish = answer['dish']
    selected_dish_id = dish_title_to_id[selected_dish]

    dish = get_dish_by_id(selected_dish_id)
    pprint(dish.serialize())
    answer = prompt([{'type': 'list', 'name': 'view', 'message': '', 'choices': [
                    'Назад']}])
    back()


def main_menu():
    main_menu_answers = {
        'Найти': find_menu,
        'Создать': create_menu,
        'Просмотреть': view_category_menu,
        'Выйти': quit_from_app,
    }
    main_menu_questions = [{
        'type': 'list',
        'name': 'main_menu',
        'message': 'Добро пожаловать в приложение!',
        'choices': ['Найти', 'Создать', 'Просмотреть', 'Выйти'],
    }]
    answer = prompt(main_menu_questions)
    clear_terminal()
    main_menu_answers[answer['main_menu']]()
    clear_terminal()


def init_client_actions():
    clear_terminal()
    work = True
    while work:
        main_menu()


def main():
    init_database()
    init_client_actions()


main()

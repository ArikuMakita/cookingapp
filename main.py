from core.init_database import init_database
import regex
from pprint import pprint
from PyInquirer import prompt

from services.DishService import (
    get_all_dish,
    create_dish,
    get_dish_by_category_id,
    get_dish_by_id
)
from services.CategoryService import get_all_category, create_category
import os
from validators import NumberValidator, RequiredValidator
from menus.return_menu.return_menu import return_menu


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_elem_choices_and_title_to_id(arr):
    elem_choices = []
    elem_title_to_id = {}
    for elem in arr:
        elem_choices.append(elem.title)
        elem_title_to_id[elem.title] = elem.id
    return elem_choices, elem_title_to_id


def back():
    return


def create_dish_menu():
    categories = get_all_category()
    category_choices, category_title_to_id = get_elem_choices_and_title_to_id(
        categories)

    create_dish_questions = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Название блюда: ',
        },
        {
            'type': 'list',
            'name': 'category',
            'message': 'Выберите категорию: ',
            'choices': category_choices,
        },
        {
            'type': 'input',
            'name': 'components',
            'message': 'Компоненты блюда (через запятую): ',
        },
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Количество порций блюда: ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'recipe',
            'message': 'Рецепт: ',
        },
        {
            'type': 'input',
            'name': 'time',
            'message': 'Время готовки блюда (в минутах): ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'calories',
            'message': 'Калорийность порции блюда: ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
    ]

    clear_terminal()
    answer = prompt(create_dish_questions)

    selected_category = answer['category']
    selected_category_id = category_title_to_id[selected_category]

    data = {
        "title": answer['title'],
        "recipe": answer['recipe'],
        "time": answer['time'],
        "calories": answer['calories'],
        "category": selected_category_id,
        "ingredients": {
            "amount": answer['amount'],
            "components": answer['components']
        }
    }

    create_dish(data)


def create_category_menu():
    create_category_questions = [{
        'type': 'input',
        'name': 'title',
        'message': 'Название категории: ',
        'validate': RequiredValidator
    }]
    clear_terminal()
    answer = prompt(create_category_questions)
    create_category(answer)


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


def quit_from_app():
    print('Чао бИбА with ❤️')
    exit()


def create_menu():
    create_menu_answers = {
        'Назад': back,
        'Новое блюдо': create_dish_menu,
        'Новая категория': create_category_menu,
    }
    create_menu_questions = [{
        'type': 'list',
        'name': 'create_menu',
        'message': 'Создать:',
        'choices': ['Назад', 'Новая категория'],
    }]
    categories = get_all_category()
    if len(categories):
        create_menu_questions[0]['choices'].append('Новое блюдо')

    answer = prompt(create_menu_questions)

    create_menu_answers[answer['create_menu']]()


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

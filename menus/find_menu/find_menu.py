from PyInquirer import prompt
from validators.RequiredValidator import RequiredValidator
from services.DishService import find_dish
from menus.view_dish_menu.view_dish_menu import view_dish_menu
from menus.return_menu.return_menu import return_menu
from utils.back import back

def find_by_title():
    answer = prompt(
        [{
            'type': 'input',
            'name': 'search',
            'message': 'Введите название: ',
            'validate': RequiredValidator
        }])
    found_dishes = find_dish({'field': 'title', 'search': answer['search']})
    if not len(found_dishes):
        return return_menu('Ничего не найдено ¯\\_(ツ)_/¯')
    return view_dish_menu(dishes=found_dishes)


def find_menu():
    find_menu_question = [{'type': 'list',
                           'name': 'find',
                           'message': 'Выберите поиск: ',
                           'choices': ["Назад", 'Название']
                           }]
    find_menu_answers = {
        'Название': find_by_title,
        'Назад': back
    }
    answer = prompt(find_menu_question)

    return find_menu_answers[answer['find']]()

from core.init_database import init_database
import regex
from pprint import pprint
from PyInquirer import prompt
from PyInquirer import Validator, ValidationError
from config import CUSTOM_TERMINAL_STYLES
from services.DishService import (
    get_all_dish,
    create_dish,
    get_dish_by_category_id,
    get_dish_by_id
)
from services.CategoryService import get_all_category, create_category
# TODO: отчистка консоли
# TODO: предложение о создании категории или блюда если их нет в просмотре 
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Пожалуйста введите целое число',
                cursor_position=len(document.text))  # Move cursor to end

def back():
    return

def create_menu__create_dish_menu():
    categories = get_all_category()
    categories_choices = []
    categories_title_to_id = {}
 
    for category in categories:
        categories_choices.append(category.title)
        categories_title_to_id[category.title] = category.id

   
    create_dish_menu_questions = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Название блюда: ',
        },
        {
            'type': 'list',
            'name': 'category',
            'message': 'Выберите категорию: ',
            'choices': categories_choices,
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
    answer = prompt(create_dish_menu_questions, style=CUSTOM_TERMINAL_STYLES)

    selected_category = answer['category']
    selected_category_id = categories_title_to_id[selected_category]

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
    

def create_menu__create_category_menu():
    category_questions = [{
            'type': 'input',
            'name': 'title',
            'message': 'Название категории: '
    }]
    clear_terminal()
    answer = prompt(category_questions, style=CUSTOM_TERMINAL_STYLES)
    create_category(answer)
    

def main_menu__find():
    print('Меню поиска')

def main_menu__view():
    categories = get_all_category()
    if not len(categories):
        print('Создайте категорию')
        answer = prompt([{'type':'list', 'name':'view','message':'','choices':['Назад']}], style=CUSTOM_TERMINAL_STYLES)
        return back()

    categories_choices = []
    categories_title_to_id = {}
 
    for category in categories:
        categories_choices.append(category.title)
        categories_title_to_id[category.title] = category.id

    view_categories_questions = [{
            'type': 'list',
            'name': 'category',
            'message': 'Выберите категорию: ',
            'choices': categories_choices,
    }]
    answer = prompt(view_categories_questions, style=CUSTOM_TERMINAL_STYLES)
    selected_category = answer['category']
    selected_category_id = categories_title_to_id[selected_category]

    dishes = get_dish_by_category_id(selected_category_id)

    if not len(dishes):
        print('Создайте блюда')
        answer = prompt([{'type':'list', 'name':'view','message':'','choices':['Назад']}], style=CUSTOM_TERMINAL_STYLES)
        return back()
    
    dishes_choices = []
    dishes_title_to_id = {}
 
    for dish in dishes:
        dishes_choices.append(dish.title)
        dishes_title_to_id[dish.title] = dish.id

    view_dish_questions = [{
            'type': 'list',
            'name': 'dish',
            'message': 'Выберите блюдо: ',
            'choices': dishes_choices,
    }]
    answer = prompt(view_dish_questions, style=CUSTOM_TERMINAL_STYLES)
    selected_dish = answer['dish']
    selected_dish_id = dishes_title_to_id[selected_dish]

    dish = get_dish_by_id(selected_dish_id)
    pprint(dish.serialize())
    answer = prompt([{'type':'list', 'name':'view','message':'','choices':['Назад']}], style=CUSTOM_TERMINAL_STYLES)
    back()


def main_menu__quit_from_app():
    print('Чао бИбА')
    exit()

def main_menu__create():
    create_menu_answers = {
        'Назад': back,
        'Новое блюдо': create_menu__create_dish_menu,
        'Новая категория': create_menu__create_category_menu,
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

    answer = prompt(create_menu_questions, style=CUSTOM_TERMINAL_STYLES)   

    create_menu_answers[answer['create_menu']]()

main_menu_answers = {
    'Найти': main_menu__find,
    'Создать': main_menu__create,
    'Просмотреть': main_menu__view,
    'Выйти': main_menu__quit_from_app,
}
main_menu_questions = [{
    'type': 'list',
    'name': 'main_menu',
    'message': 'Добро пожаловать в приложение!',
    'choices': ['Найти', 'Создать', 'Просмотреть', 'Выйти'],
}]


def init_client_actions():
    clear_terminal()
    work = True
    while work:
        answer = prompt(main_menu_questions, style=CUSTOM_TERMINAL_STYLES)
        clear_terminal()
        main_menu_answers[answer['main_menu']]()
        clear_terminal()

def main():
    init_database()
    init_client_actions()

main()
from PyInquirer import prompt
from utils.back import back
from menus.create_dish_menu.create_dish_menu import create_dish_menu
from menus.create_category_menu.create_category_menu import create_category_menu
from services.CategoryService import get_all_category

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
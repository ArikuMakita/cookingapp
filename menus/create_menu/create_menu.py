from services.CategoryService import get_all_category
from .create_menu_questions import get_create_menu_questions
from .create_menu_answers import CREATE_MENU_ANSWERS
from PyInquirer import prompt

def create_menu():
    categories = get_all_category()
    create_menu_questions = get_create_menu_questions()
    if len(categories):
        create_menu_questions[0]['choices'].append('Новое блюдо')

    answer = prompt(create_menu_questions)

    CREATE_MENU_ANSWERS[answer['create_menu']]()
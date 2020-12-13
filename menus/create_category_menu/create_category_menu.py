from utils.clear_terminal import clear_terminal
from PyInquirer import prompt
from .create_category_questions import CREATE_CATEGORY_QUESTIONS
from services.CategoryService import create_category


def create_category_menu():
    
    clear_terminal()
    answer = prompt(CREATE_CATEGORY_QUESTIONS)
    create_category(answer)

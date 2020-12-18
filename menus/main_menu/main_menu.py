from PyInquirer import prompt
from .main_menu_questions import MAIN_MENU_QUESTIONS
from .main_menu_answers import MAIN_MENU_ANSWERS
from utils.clear_terminal import clear_terminal

def main_menu():
    answer = prompt(MAIN_MENU_QUESTIONS)
    clear_terminal()
    MAIN_MENU_ANSWERS[answer['main_menu']]()
    clear_terminal()
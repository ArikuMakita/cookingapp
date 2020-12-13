from .return_answers import *
from .return_questions import *
from PyInquirer import prompt

def return_menu(msg):
    print(msg)
    answer = prompt(return_questions)
    return return_aswers[answer['return_menu']]()

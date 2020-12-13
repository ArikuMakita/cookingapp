from .return_answers import RETURN_ANSWERS
from .return_questions import RETURN_QUESTIONS
from PyInquirer import prompt

def return_menu(msg):
    print(msg)
    answer = prompt(RETURN_QUESTIONS)
    return RETURN_ANSWERS[answer['return_menu']]()

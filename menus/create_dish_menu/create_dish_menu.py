from services.DishService import create_dish
from utils.get_elem_choices_and_title_to_id import get_elem_choices_and_title_to_id
from .create_dish_questions import get_create_dish_questions
from services.CategoryService import get_all_category
from utils.clear_terminal import clear_terminal
from PyInquirer import prompt
from pprint import pprint

def create_dish_menu():
    categories = get_all_category()
    category_choices, category_title_to_id = get_elem_choices_and_title_to_id(
        categories)

    create_dish_questions = get_create_dish_questions(category_choices)

    clear_terminal()
    answer = prompt(create_dish_questions)

    selected_category = answer['category']
    selected_category_id = category_title_to_id[selected_category]
    pprint(answer)
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

from .view_category_questions import get_view_category_questions
from services.CategoryService import get_all_category
from utils.get_elem_choices_and_title_to_id import get_elem_choices_and_title_to_id
from PyInquirer import prompt
from menus.view_category_menu.view_category_questions import get_view_category_questions
from menus.view_dish_menu.view_dish_questions import get_view_dish_questions
from menus.view_dish_menu.view_dish_menu import view_dish_menu
from menus.return_menu.return_menu import return_menu


def view_category_menu():

    categories = get_all_category()
    if not len(categories):
        return return_menu('Создайте категорию')

    category_choices, category_title_to_id = get_elem_choices_and_title_to_id(
        categories)

    view_category_questions = get_view_category_questions(category_choices)

    answer = prompt(view_category_questions)
    selected_category = answer['category']
    selected_category_id = category_title_to_id[selected_category]

    return view_dish_menu(selected_category_id)
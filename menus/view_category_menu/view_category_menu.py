from .view_category_questions import get_view_category_questions
from services.CategoryService import get_all_category
from utils.get_elem_choices_and_title_to_id import get_elem_choices_and_title_to_id
from PyInquirer import prompt
from menus.view_category_menu.view_category_questions import get_view_category_questions
from menus.view_dish_menu.view_dish_questions import get_view_dish_questions
from menus.view_dish_menu.view_dish_menu import view_dish_menu
from menus.return_menu.return_menu import return_menu
from utils.back import back
from services.CategoryService import delete_category_by_id
from utils.confirnamion import isComfirmed


def view_category_menu(isDelete=None):
    categories = get_all_category()
    if not len(categories):
        return return_menu('Создайте категорию')
    category_choices, category_title_to_id = get_elem_choices_and_title_to_id(
        categories)
    view_category_questions = get_view_category_questions(category_choices)

    if isDelete:
        view_category_questions[0]['choices'].remove('Удалить')

    answer = prompt(view_category_questions)
    selected_category = answer['category']
    if selected_category == "Назад":
        return back()
    if selected_category == "Удалить":
        return view_category_menu(isDelete=True)

    selected_category_id = category_title_to_id[selected_category]

    if isDelete:
        if isComfirmed():
            delete_category_by_id(selected_category_id)
        return back()

    return view_dish_menu(selected_category_id)

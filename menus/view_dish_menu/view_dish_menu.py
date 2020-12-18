from services.DishService import get_dish_by_category_id, get_dish_by_id
from menus.return_menu.return_menu import return_menu
from utils.get_elem_choices_and_title_to_id import get_elem_choices_and_title_to_id
from menus.view_dish_menu.view_dish_questions import get_view_dish_questions
from PyInquirer import prompt
from pprint import pprint
from utils.back import back


def view_dish_menu(selected_category_id):
    dishes = get_dish_by_category_id(selected_category_id)
    if not len(dishes):
        return return_menu('Создайте блюда')

    view_dish_choices, dish_title_to_id = get_elem_choices_and_title_to_id(
        dishes)

    view_dish_questions = get_view_dish_questions(view_dish_choices)

    answer = prompt(view_dish_questions)
    selected_dish = answer['dish']
    if selected_dish == "Назад":
        return back()
    selected_dish_id = dish_title_to_id[selected_dish]

    # TODO: Создать view_dish

    dish = get_dish_by_id(selected_dish_id)
    pprint(dish.serialize())
    answer = prompt([{'type': 'list', 'name': 'view', 'message': '', 'choices': [
                    'Назад']}])
    return back()
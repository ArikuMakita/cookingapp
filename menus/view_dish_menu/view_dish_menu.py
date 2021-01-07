from services.DishService import get_dish_by_category_id, get_dish_by_id
from menus.return_menu.return_menu import return_menu
from utils.get_elem_choices_and_title_to_id import get_elem_choices_and_title_to_id
from menus.view_dish_menu.view_dish_questions import get_view_dish_questions
from PyInquirer import prompt
from pprint import pprint
from utils.back import back
from utils.clear_terminal import clear_terminal
from .view_dish_answers import VIEW_DISH_ANSWERS


def view_dish_menu(selected_category_id=None, dishes=None):
    if dishes is None:
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

    dish = get_dish_by_id(selected_dish_id)
    clear_terminal()
    print(f"Название: {dish.title}")
    print(f"Рецепт: {dish.recipe}")
    print(f"Время приготовления: {dish.time} минут")
    print(f"Калории: {dish.calories}")
    print(f"Категория: {dish.category.title}")
    print(f"Количество порций: {dish.ingredients.amount}")
    print(f"Ингредиенты блюда: {dish.ingredients.components}")


    answer = prompt([{'type': 'list', 'name': 'view', 'message': '', 'choices':
                      ['Редактировать', 'Удалить', 'Назад']}])
    return VIEW_DISH_ANSWERS[answer['view']](dish)

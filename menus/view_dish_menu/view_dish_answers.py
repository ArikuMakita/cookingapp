from utils.back import back
from menus.create_dish_menu.create_dish_questions import get_create_dish_questions
from PyInquirer import prompt
from pprint import pprint
from services.DishService import edit_dish_by_id, edit_ingredients_by_id
from utils.clear_terminal import clear_terminal
from services.DishService import delete_dish_by_id
from utils.confirnamion import isComfirmed


def edit_menu(dish):
    clear_terminal()
    create_dish_questions = get_create_dish_questions(
        default_values=dish.serialize())
    answer = prompt(create_dish_questions)

    edited_dish = {
        "title": answer['title'],
        "recipe": answer['recipe'],
        "time": answer['time'],
        "calories": answer['calories']
    }

    edited_ingredients = {
        "amount": answer['amount'],
        "components": answer['components']
    }
    edit_dish_by_id(dish.id, edited_dish)
    edit_ingredients_by_id(dish.ingredients, edited_ingredients)


def delete_menu(dish):
    if not isComfirmed():
        return

    delete_dish_by_id(dish.id)


VIEW_DISH_ANSWERS = {
    'Редактировать': edit_menu,
    'Удалить': delete_menu,
    'Назад': back
}

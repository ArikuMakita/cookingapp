def get_view_dish_questions(view_dish_choices):
    return [{
        'type': 'list',
        'name': 'dish',
        'message': 'Выберите блюдо: ',
        'choices': ["Назад"] + view_dish_choices,
        }]
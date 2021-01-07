from validators.NumberValidator import NumberValidator
from validators.RequiredValidator import RequiredValidator


def get_default_value_by_key(default_values, key):
    keys = key.split('.')
    default_value = ''
    try:
        if len(keys) == 1:
            default_value = default_values[keys[0]]
        elif len(keys) == 2:
            default_value = default_values[keys[0]][keys[1]]
        return str(default_value)
    except KeyError:
        return default_value


def get_create_dish_questions(category_choices=None, default_values={}):
    dish_questions = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Название блюда: ',
            'default': get_default_value_by_key(default_values, 'title'),
            'validate': RequiredValidator
        },

        {
            'type': 'input',
            'name': 'components',
            'default': get_default_value_by_key(default_values, 'ingredients.components'),
            'message': 'Компоненты блюда (через запятую): ',
            'validate': RequiredValidator

        },
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Количество порций блюда: ',
            'default': get_default_value_by_key(default_values, 'ingredients.amount'),
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'recipe',
            'default': get_default_value_by_key(default_values, 'recipe'),
            'message': 'Рецепт: ',
            'validate': RequiredValidator
        },
        {
            'type': 'input',
            'name': 'time',
            'message': 'Время готовки блюда (в минутах): ',
            'default': get_default_value_by_key(default_values, 'time'),
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'calories',
            'message': 'Калорийность порции блюда: ',
            'default': get_default_value_by_key(default_values, 'calories'),
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
    ]
    if category_choices is not None:
        dish_questions.insert(1, {
            'type': 'list',
            'name': 'category',
            'message': 'Выберите категорию: ',
            'choices': category_choices,
        })
    return dish_questions

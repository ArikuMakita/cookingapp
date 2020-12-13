from validators.NumberValidator import NumberValidator
from validators.RequiredValidator import RequiredValidator

def get_create_dish_questions(category_choices):
    return [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Название блюда: ',
            'validate': RequiredValidator
        },
        {
            'type': 'list',
            'name': 'category',
            'message': 'Выберите категорию: ',
            'choices': category_choices,
        },
        {
            'type': 'input',
            'name': 'components',
            'message': 'Компоненты блюда (через запятую): ',
            'validate': RequiredValidator
            
        },
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Количество порций блюда: ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'recipe',
            'message': 'Рецепт: ',
            'validate': RequiredValidator
        },
        {
            'type': 'input',
            'name': 'time',
            'message': 'Время готовки блюда (в минутах): ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'calories',
            'message': 'Калорийность порции блюда: ',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
    ]

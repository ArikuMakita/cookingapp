def get_view_category_questions(category_choices):
    return [{
        'type': 'list',
        'name': 'category',
        'message': 'Выберите категорию: ',
        'choices': ["Назад", 'Удалить'] + category_choices,
    }]

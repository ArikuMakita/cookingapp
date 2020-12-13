from validators.RequiredValidator import RequiredValidator


CREATE_CATEGORY_QUESTIONS = [{
    'type': 'input',
    'name': 'title',
    'message': 'Название категории: ',
    'validate': RequiredValidator
}]

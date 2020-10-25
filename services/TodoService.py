from models.Todo import Todo


def create_todo(data):
    """
        Создает Todo
        Принимает словарь data {title:'title'}
        Бросает ошибку, если data не соответствует требованиям
    """
    _validate_todo(data)
    return Todo.create(title=data['title'])


def get_all_todo():
    """
        Возвращает список всех todo
    """
    query_todos = Todo.select()
    return [todo for todo in query_todos]


def get_todo_by_id(id):
    '''
        Возвращает todo с идентификатором id
        Бросит ошибку, если такого нет
    '''
    _check_if_exists(id)
    return Todo.get_by_id(id)


def delete_todo_by_id(id):
    """
        Удаляет todo с идентификатором id
        Бросит ошибку, если такого нет
    """
    _check_if_exists(id)
    Todo.get(Todo.id == id).delete_instance()


def _check_if_exists(id):
    '''
        Проверят наличие todo c идентификатором id
        Если нет, то выбрасывает ошибку
    '''
    try:
        Todo.get_by_id(id)
    except Todo.DoesNotExist:
        raise Exception(f'Todo with id={id} does not exist')


def _validate_todo(data):
    '''
        Проверят соответствует ли данные data требованиям
    '''
    if not len(data['title']):
        raise Exception('Title was not provided!')

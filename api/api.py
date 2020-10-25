import eel
import json
from services.TodoService import (
    create_todo,
    get_all_todo,
    delete_todo_by_id,
)


@eel.expose
def addTodo(data="{'title':''}"):
    '''
        Создает Todo
        Принимает JSON строку вида {title:''}
    '''
    data = json.loads(data)
    new_todo = create_todo(data)
    new_json_todo = json.dumps(new_todo.serialize())
    return new_json_todo


@eel.expose
def deleteTodoById(data="{'id':0}"):
    '''
        Удаляет Todo по id
        Принимает JSON строку вида {'id':0}
    '''
    data = json.loads(data)
    return delete_todo_by_id(data['id'])


@eel.expose
def getAllTodo():
    '''
        Возвращает все Todo
    '''
    todos = get_all_todo()
    json_todos = json.dumps([todo.serialize() for todo in todos])
    return json_todos

import eel
from core.init_database import init_database
from api import api

init_database()



# ! Проверять сервисы так:
from services.TodoService import get_all_todo
todos = get_all_todo()
serialized_todos = []
for todo in todos:
    serialized_todos.append(todo.serialize())

exit()

eel.init('web')

page = 'main.html'
size = (700, 700)

try:
    eel.start(page, size=size)
except:
    # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    import sys
    import platform

    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start(page, mode='edge', size=size)
    else:
        raise

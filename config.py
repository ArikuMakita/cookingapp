from models.Todo import Todo
from utils.get_database_path import get_database_path

DATABASE = 'my_db.db'
APP_NAME = 'todoapp'

MODELS = (
    Todo,
)

DATABASE_PATH = get_database_path(appname=APP_NAME, database=DATABASE)

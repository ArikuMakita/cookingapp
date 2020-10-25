from models.Todo import Todo
from models.Category import Category
from models.Dish import Dish
from models.Ingridients import Ingridients

from utils.get_database_path import get_database_path

DATABASE = 'my_db.db'
APP_NAME = 'todoapp'

MODELS = (
    Todo,
    Category,
    Dish,
    Ingridients
)

# DATABASE_PATH = get_database_path(appname=APP_NAME, database=DATABASE)
DATABASE_PATH = 'my.db'

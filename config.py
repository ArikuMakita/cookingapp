from models.Category import Category
from models.Dish import Dish
from models.Ingredients import Ingredients
from utils.get_database_path import get_database_path

DATABASE = 'my.db'
APP_NAME = 'todoapp'

MODELS = (
    Category,
    Dish,
    Ingredients
)

# DATABASE_PATH = get_database_path(appname=APP_NAME, database=DATABASE)
DATABASE_PATH = 'my.db'


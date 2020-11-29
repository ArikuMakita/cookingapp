from models.Todo import Todo
from models.Category import Category
from models.Dish import Dish
from models.Ingredients import Ingredients
from PyInquirer import style_from_dict, Token
from utils.get_database_path import get_database_path

DATABASE = 'my.db'
APP_NAME = 'todoapp'

MODELS = (
    Todo,
    Category,
    Dish,
    Ingredients
)

# DATABASE_PATH = get_database_path(appname=APP_NAME, database=DATABASE)
DATABASE_PATH = 'my.db'

CUSTOM_TERMINAL_STYLES = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})
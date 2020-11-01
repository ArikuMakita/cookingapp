from peewee import InternalError, SqliteDatabase
from config import MODELS, DATABASE_PATH


def get_database():
    '''
        Возвращает базу данных
    '''
    sqlite_db = SqliteDatabase(DATABASE_PATH, pragmas={'journal_mode': 'wal'})
    return sqlite_db


def connect_to_data_base(database):
    '''
        Устанавливает подключение к переданной database базе данных
    '''
    database.connect()


def create_tables_if_not_exists(database, models):
    '''
        Создает таблицы в базе данных если их нет
        Принимает словарь моделей models - наследников BaseModel
    '''
    for Model in models:
        Model._meta.database = database
        Model.create_table()


def init_database():
    ''' 
        Создает подключение к базе данных,
        Создает таблицы, если их нет
    '''
    try:
        database = get_database()
        connect_to_data_base(database)
        create_tables_if_not_exists(database, MODELS)
    except Exception as e:
        print('--Init error--')
        print(e)
        print('--Init error ended!--')

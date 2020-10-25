from peewee import Model


class BaseModel(Model):
    '''
        Базовая модель, от которой необходимо наследоваться для создания моделей
    '''

    def serialize(self):
        raise NotImplementedError(
            f'Метод serialize должен быть определён в {self.__class__.__name__}.')

from peewee import CharField
from core.BaseModel import BaseModel


class Todo(BaseModel):
    '''
        Модель Todo с полями:
            Заголовок title(max_length=100)
    '''
    title = CharField(max_length=100)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title
        }

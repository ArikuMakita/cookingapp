from peewee import CharField
from core.BaseModel import BaseModel


class Category(BaseModel):
    """
    Модель категорий.
    Поля: title, id
    """
    title = CharField(max_length=100)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
        }

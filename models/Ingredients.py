from peewee import (
    CharField,
    IntegerField,
    TextField
)
from core.BaseModel import BaseModel


class Ingredients(BaseModel):
    """
    Модель состава.
    Поля: id, amount,
        components = 'Компонент 1; Компонент 2'
    """
    amount = IntegerField()
    components = TextField()

    def serialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'components': self.components
        }

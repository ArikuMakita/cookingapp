from peewee import (
    CharField,
    IntegerField,
    TextField,
    ForeignKeyField
)
from core.BaseModel import BaseModel
from .Category import Category
from .Ingridients import Ingridients


class Dish(BaseModel):
    title = CharField(max_length=100)
    recipe = TextField()
    time = IntegerField()
    calories = IntegerField()
    category = ForeignKeyField(Category)
    ingridients = ForeignKeyField(Ingridients)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': self.recipe,
            'time': self.time,
            'calories': self.calories,
            'category': self.category.serialize(),
            'ingridients': self.ingridients.serialize()
        }

from peewee import (
    CharField,
    IntegerField,
    TextField,
    ForeignKeyField
)
from core.BaseModel import BaseModel
from .Category import Category
from .Ingredients import Ingredients


class Dish(BaseModel):
    title = CharField(max_length=100)
    recipe = TextField()
    time = IntegerField()
    calories = IntegerField()
    category = ForeignKeyField(Category)
    ingredients = ForeignKeyField(Ingredients)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': self.recipe,
            'time': self.time,
            'calories': self.calories,
            'category': self.category.serialize(),
            'ingredients': self.ingredients.serialize()
        }

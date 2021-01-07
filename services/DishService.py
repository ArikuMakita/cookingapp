from models.Dish import Dish
from models.Ingredients import Ingredients
from models.Category import Category
from utils.get_model_field import get_model_field
from utils.transform_user_dict_to_valid_dict import transform_user_dict_to_valid_dict
from utils.transform_query_to_array import transform_query_to_array


def find_dish(data):
    """
    data = {field, search}
    """
    field = data['field']
    search = data['search']

    if field == 'category':
        category = Category.get(Category.title == search)
        search = category.id
    query_dish = Dish.select().where(get_model_field(Dish, field) == search)
    return transform_query_to_array(query_dish)


def create_dish(data):
    """
    data = {
        title: str,
        recipe: str,
        time: int,
        calories: int,
        category: int,
        ingredients: {
            amount: int,
            components: str
        }
    }
    """
    ingredients = Ingredients.create(
        amount=data['ingredients']['amount'],
        components=data['ingredients']['components'])

    dish = Dish.create(
        title=data['title'],
        recipe=data['recipe'],
        time=data['time'],
        calories=data['calories'],
        category=data['category'],
        ingredients=ingredients)

    return dish


def edit_dish_by_id(id, data):
    """
    id: int
    data: {
        title: 'some title'
    }
    """
    valid_data = transform_user_dict_to_valid_dict(Dish, data)
    dish = Dish.update(valid_data).where(Dish.id == id).execute()
    return dish


def edit_ingredients_by_id(id, data):
    valid_data = transform_user_dict_to_valid_dict(Ingredients, data)
    ingredients = Ingredients.update(valid_data).where(Ingredients.id == id).execute()
    return ingredients


def get_all_dish():
    query_dish = Dish.select()
    return transform_query_to_array(query_dish)


def get_dish_by_category_id(category_id):
    query_dish = Dish.select().where(Dish.category_id == category_id)
    return transform_query_to_array(query_dish)


def get_dish_by_id(id):
    return Dish.get_by_id(id)


def delete_dish_by_id(id):
    dish = get_dish_by_id(id)
    Ingredients.get_by_id(dish.ingredients).delete_instance()
    dish.delete_instance()



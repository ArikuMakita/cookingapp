from models.Category import Category
from utils.transform_user_dict_to_valid_dict import transform_user_dict_to_valid_dict
from utils.transform_query_to_array import transform_query_to_array


def create_category(data):
    """
    data = {
        title
    }
    """
    category = Category.create(title=data['title'])
    return category


def edit_category_by_id(id, data):
    valid_data = transform_user_dict_to_valid_dict(Category, data)
    category = Category.update(valid_data).where(Category.id == id).execute()
    return category


def delete_category_by_id(id):
    Category.get_by_id(id).delete_instance()


def get_all_category():
    # Верни список категорий
    query_category = Category.select()
    return transform_query_to_array(query_category)

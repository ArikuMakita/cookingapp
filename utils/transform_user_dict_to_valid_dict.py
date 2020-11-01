from .get_model_field import get_model_field


def transform_user_dict_to_valid_dict(model, user_dict):
    valid_dict = {}
    dict_items = user_dict.items()
    for key, value in dict_items:
        valid_dict[get_model_field(model, key)] = value
    return valid_dict

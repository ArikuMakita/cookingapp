def get_elem_choices_and_title_to_id(arr):
    elem_choices = []
    elem_title_to_id = {}
    for elem in arr:
        elem_choices.append(elem.title)
        elem_title_to_id[elem.title] = elem.id
    return elem_choices, elem_title_to_id

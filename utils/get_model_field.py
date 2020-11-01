def get_model_field(model, field):
    try:
        return getattr(model, field)
    except:
        raise Exception(f'No field: {field}')
FIELDS = ('name', 'age', 'color')


def check_field_is_in_response(response_data):
    for key in FIELDS:
        if key not in response_data:
            return False
    return True


def check_unexpected_field_not_in_response(response_data):
    for key in response_data.keys():
        if key not in FIELDS:
            return False
    return True


def check_cat_exists(cat):
    return cat is not None

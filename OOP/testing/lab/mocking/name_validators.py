
class ValidationException(Exception):
    pass

MIN_LEN = 2
MAX_LEN = 30

def validate_name(name):
    if name is None:
        raise ValidationException('Name cannot be "None"')

    if not isinstance(name, str):
        raise ValidationException('Name must be string')

    the_lenght = len(name)
    if the_lenght < MIN_LEN or MAX_LEN < the_lenght:
        raise ValidationException('Name should be between 2 and 30 symbols.')

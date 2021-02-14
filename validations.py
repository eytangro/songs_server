
from users import Users


def valid_parameters(**kwargs):
    for key, value in kwargs.items():
        if value is None:
            return {
                "error": f"Misssing parameter {key}"
            }
    return True


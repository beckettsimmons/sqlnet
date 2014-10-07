def use_docstring_from(from_obj):
    """ Generates decorator that inherits a docstring.

    Args:
        obj (object): The python object to inherit docstring from.
    """
    def decorator(to_obj):
        to_obj.__doc__ = from_obj.__doc__
        return to_obj
    return decorator

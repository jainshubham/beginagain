import inspect


def get_choices(enum_class):
    """ generate choices for model's class field.

    :param enum_class: Either IntEnum or Enum class
    :return: tuple(
    examples;- In case of IntEnum class
    ((3, 'BOOLEAN'), (2, 'DATETIME'), (0, 'INTEGER'), (1, 'STRING')) or
    In case of Enum class
    (('A', 'BOOLEAN'), ('B', 'DATETIME'), ('C', 'INTEGER'), ('D', 'STRING'))
    )
    """
    # get all members of the class
    members = inspect.getmembers(enum_class, lambda m: not(inspect.isroutine(m)))
    # filter down to just properties
    props = [m for m in members if not(m[0][:2] == '__')]
    # format into django choice tuple
    choices = tuple([(p[1].value, p[0].replace('_', ' ').title()) for p in props])
    return choices

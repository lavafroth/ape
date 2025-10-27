import inspect


def AlgebraicEnum(cls):
    for subclass_name, subclass in inspect.getmembers(cls, predicate=inspect.isclass):
        if subclass_name != "__class__":
            setattr(cls, subclass_name, type(subclass_name, (cls, subclass), {}))

    return cls


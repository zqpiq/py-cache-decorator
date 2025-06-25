from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in result:
            print("Calculating new result")
        else:
            print("Getting from cache")
            result[key] = func(*args, **kwargs)
        return result[key]
    return wrapper

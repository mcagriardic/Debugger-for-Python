from functools import wraps

c = 0
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global c
        c += 1
        print(
            f"Call {c} with: {args if args else ''},"
            f"{kwargs if kwargs else ''}"
        )
        res = func(*args, **kwargs)
        print(
            f"for {args if args else ''}"
            f"{kwargs if kwargs else ''} -> returns: {res!r}"
        )
        return res
    return wrapper
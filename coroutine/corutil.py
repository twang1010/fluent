from functools import wraps

def coroutine(func):
    @wraps(func)
    def primer(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    return primer


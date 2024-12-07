import functools

from mediatheory.log import logging


def _decorator_log(func, args, rw):
    logging.info(f"[{rw}] " + str(func).split()[1] + f"{args}")


def read(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _decorator_log(func, args, "R")
        return func(*args, **kwargs)

    return wrapper


def write(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        _decorator_log(func, args, "W")
        return func(*args, **kwargs)

    return wrapper


def staticread(func):
    return staticmethod(read(func))


def staticwrite(func):
    return staticmethod(write(func))

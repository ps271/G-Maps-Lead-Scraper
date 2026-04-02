import os


def get_env(name, default=None):
    return os.getenv(name, default)


def get_bool(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.lower() in ("true", "1", "yes")


def get_int(name, default=0):
    value = os.getenv(name)
    if value is None:
        return default
    return int(value)


def get_list(name, separator=","):
    value = os.getenv(name)
    if not value:
        return []
    return [item.strip() for item in value.split(separator)]
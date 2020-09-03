import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper
from functools import wraps


def as_dict(func):
    """
    return type이 Union[ORM, List[ORM], None]인 경우에 사용.
    {"data": ...} 의 형태로 리턴한다.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is None:
            return {}
        elif type(res) == list:
            return {"data": [x.__dict__ for x in res]}
        else:
            return {"data": res.__dict__}

    return wrapper

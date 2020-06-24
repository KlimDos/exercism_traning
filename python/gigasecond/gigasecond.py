from datetime import timedelta

def add(moment: object) -> object:
    result = moment + timedelta(seconds=10 ** 9)
    return result

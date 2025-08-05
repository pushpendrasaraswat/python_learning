
def make_bold(func):
    def wrapper():
        return f'<h1><b>{func()}</h1>'
    return wrapper


def make_italic(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper

def make_underline(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__} {args}")
        result = func(*args, **kwargs)
        print(f"It returned: {result}")
        return result
    return wrapper


@logging_decorator
def a_function_to_decorate(*args):
    return sum(args)


a_function_to_decorate(4, 5, 6)
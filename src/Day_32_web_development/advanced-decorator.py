
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def __str__(self):
        return f"User: {self.name}"

    def decorator_wrapper(function):
        def wrapper(*args, **kwargs):
            print(f"you caled {function.__name__} with arguments: {args} and keyword arguments: {kwargs}")
            if args[0].is_logged_in:
               return function(args[0])
        return wrapper

    @decorator_wrapper
    def create_blob_post(user):
        return f"This is a log for {user.name}."



user = User("John Doe")
user.is_logged_in = True
print(user.create_blob_post(user))

print(user)
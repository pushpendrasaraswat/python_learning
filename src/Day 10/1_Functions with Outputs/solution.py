def say_hello():
    return "Hello World!"


print(say_hello())


def format_name(f_name, l_name):
    return f_name.title() + " " + l_name.title() # title() capitalizes the first letter of each word


print(format_name("AnGeLa", "YU"))


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)


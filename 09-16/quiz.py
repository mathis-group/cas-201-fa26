# This quiz is focused on understanding return types
# Think carefully about what these functions do.

def func1(name):
    print(f"Hello {name}!")
    return f"Goodbye {name}!"


def func2(name):
    return f"Hello {name}!"


a = func2("Joe")
b = func1("Mary")
print(a)
print(b)
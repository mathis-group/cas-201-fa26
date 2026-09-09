# The first function you saw
# y = print("Hello World!", "This is a function example.")
# print(y, type(y))

# You've seen the type function too
x = 10
type_x = type(x)
# print(x, type_x)

# We can write our own functions too
def my_add(a, b):
    y = 100 
    print(y)
    x = a + b
    return x

def add_print(a,b):
    x = a + b
    print(x)

# x = my_add(10, 20)
# print(x) 

# y = add_print(10, 20)
# print(y)

# The anatomy of a function:
def any_name(arg1, arg2):

    something = arg1 * 10 + arg2
    return something 

# This function takes integers
s = any_name(10, 20)
# print(s)

# This function takes strings
s2 = any_name("Hello", "World")
# print(s2)

# This function could take floats
s3 = any_name(10.5, 20.5)
# print(s3)

# booleans?
s4 = any_name(True, False)
# print(s4)

# Scope example
y = 1

s = my_add(10, 20)

print(y)
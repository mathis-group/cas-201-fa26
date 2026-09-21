def quiz_func(arg1, arg2):
    combined_args = arg1 + 3*arg2
    return combined_args

a = quiz_func(2,3)
print(f'a = {a}')

b = quiz_func(10,2)
b_output = f"b = {b}"
print(b_output)

c = quiz_func("Hello","Functions")
print(f"c = {c}")
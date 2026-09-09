a = 3
# print("a =", a)
# a = a + 2
# a -= 2
# a += 2
# print("a =", a)

name = "Cole"
name += " Mathis"
# print("name =", name)

def add2(x):
    q = 10
    f = 100
    z = q + f + x
    new = x + 2
    return new, q

y, z = add2(3)
# print("y =", y)
# print("z =", z)

def my_func(x, y):
    a = 10
    print("a in the LOCAL SCOPE =", a)
    return x + y, x * y

# print("a in the GLOBAL SCOPE =", a)
sum, diff = my_func(3, 5)
print("sum =", sum)
print("diff =", diff)

def my_func2(x, y):
    x = x + y

x = 3 
z = my_func2(x, 5)
print("z =", z)
print("x =", x)
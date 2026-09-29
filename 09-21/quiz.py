a = 0
b = 1

while a < 5:
    print(f"a = {a}")
    print(f"b = {b}")
    print("-----")

    # If a is even, a % 2 == 0 
    if a % 2 == 0:
        b = a + b
        a +=1

    else:
        b += 1
        a += 1

print(f"The final value of a is {a}")
print(f"The final value of b is {b}")
def fib(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_numbers = {0: 1, 1: 1}

for i in range(2,10):
    fib_numbers[i] = fib(i)

print(f"fib_numbers = {fib_numbers}")

def fib(n):
    #""" Return the nth fibinaicci number"""
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    fibs = [1,1]
    for i in range(2,n+1):
        new_fib = fibs[i-1] + fibs[i-2]
        fibs.append(new_fib)
        #print(fibs)
    return fibs[-1]

print(f"fib(5) = {fib(5)}")
print(f"fib(6) = {fib(6)}")
#print(f"fib2(40) = {fib2(40)}")
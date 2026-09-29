def fib(n):
    # This function will produce the first n numbers in the fibonacci sequence
    # The sequence starts with 1,1, and each subsequent number is formed by taking
    # the sum of the previous two. 

    fib_nums = [1,1] # start the sequence

    for i in range(1,n-1):
        
        new_fib = fib_nums[i] + fib_nums[i-1] # Make the next step
        print(f"i = {i}, new_fib = {new_fib}")
        #print(f"At this step fib_nums started as {fib_nums}")
        fib_nums.append(new_fib)
        #print(f"and fib_nums became {fib_nums}")
        # print("----")

    return fib_nums

my_fibs = fib(5)
print(f"my_fibs = {my_fibs}")
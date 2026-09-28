
list_a = [1,3,4,5,7,10,9,8,6]

list_b = [10,1,2,3,4,5,6,7,8,9]

list_c = [1,2,3,4,5,10,9,8,7,6]

# Python sorting
sorted_a = sorted(list_a)
sorted_b = sorted(list_b)
sorted_c = sorted(list_c)

def is_sorted(my_list):
    # Return True if my_list is sorted
    # Return False if my_list is not sorted
    n = len(my_list)
    for i in range(n-1):
        if my_list[i+1] <= my_list[i]:
            return False
        
    return True

def push_to_end(my_list, i):
    n = len(my_list)
    if i <= n:
        value = my_list.pop(i)
        my_list.append(value)
        return my_list
    else:
        raise ValueError("i is bigger than n; that won't work.")

def swap_idx(my_list, i, j):
    # This will return my_list with the elements at i and j swapped
    n = len(my_list)
    if (i <= n) and (j <= n):
        # Swap them
        holder = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = holder
        #  
    else:
        raise ValueError("i or j is bigger than n; that won't work")

    return my_list

print(f"list_a = {list_a}")
print(f"list_a is sorted: {is_sorted(list_a)}")
print(f"sorted_a = {sorted_a}")
print(f"sorted_a is sorted: {is_sorted(sorted_a)}")

print(f"swap_idx(list_a, 1, 6) = {swap_idx(list_a, 1, 6)}")
print(f"push_to_end(list_a, 1) = {push_to_end(list_a, 1)}")

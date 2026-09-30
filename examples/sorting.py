import random
list_a = [1,3,4,5,7,10,9,8,6]

list_b = [10,1,2,3,4,5,6,7,8,9]

list_c = [1,2,3,4,5,10,9,8,7,6]

# Python sorting
sorted_a = sorted(list_a)
sorted_b = sorted(list_b)
sorted_c = sorted(list_c)

def our_sort(my_list):
    # Our sorting algorithm
    n = len(my_list)
    # is the list sorted?
    complete = is_sorted(my_list)
    while not complete:
        for i in range(n-1):
            if my_list[i] > my_list[i+1]:
                my_list = push_to_end(my_list, i)

        print(f"current list: {my_list}")
        complete = is_sorted(my_list)

    return my_list

def bubble_sort(my_list):
    # Our sorting algorithm
    n = len(my_list)
    # is the list sorted?
    complete = is_sorted(my_list)
    while not complete:
        for i in range(n-1):
            if my_list[i] > my_list[i+1]:
                my_list = swap_idx(my_list, i, i+1)

        # print(f"current list: {my_list}")
        complete = is_sorted(my_list)

    return my_list

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
  
    else:
        raise ValueError("i or j is bigger than n; that won't work")

    return my_list

# print(f"list_a = {list_a}")
# print(f"list_a is sorted: {is_sorted(list_a)}")
# print(f"sorted_a = {sorted_a}")
# print(f"sorted_a is sorted: {is_sorted(sorted_a)}")

# print(f"swap_idx(list_a, 1, 6) = {swap_idx(list_a, 1, 6)}")
# # print(f"push_to_end(list_a, 1) = {push_to_end(list_a, 1)}")
# print(f" Sort by pushing to the end")
# print(f"starting list: {list_c}")
# our_sort(list_c)
# print(f"final list: {list_c}")

# print("-----------")
# print(f"Sort by swapping")
# print(f"starting list: {list_a}")
# bubble_sort(list_a)
# print(f"final list: {list_a}")

# Make a big random list
N = 10000
big_list = random.sample(range(N),N)
# print(f"{bubble_sort(big_list)}")
# print(f"big_list = {big_list}")

### Why is this so slow? What could we do differently?

list_1 = [1, 5, 10]
list_2 = [2, 20, 30]

list_1_2 = [1, 2, 5, 10, 20, 30]

merged_list = []

def merge_sorted(list1, list2):
    merged_list = []

    while (len(list1) > 0) and (len(list2) > 0): 
        print(f"list_1 = {list_1}")
        print(f"list_2 = {list_2}")
        print("_____")

        if list_1[0] < list_2[0]:
            e = list_1.pop(0)
            merged_list.append(e)
        else:
            e = list_2.pop(0)
            merged_list.append(e)

        print(f"list_1 = {list_1}")
        print(f"list_2 = {list_2}")
        print(f"merged_list = {merged_list}")
        print("\n \n")

    if len(list1) > 0:
        merged_list += list1
    if len(list2) > 0:
        merged_list += list2
    print(f"merged_list = {merged_list}")

merge_sorted(list_1, list_2)
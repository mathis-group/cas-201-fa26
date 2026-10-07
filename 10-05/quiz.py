list_1 = [1, 2, 3, 4, 5, 9, 10]
list_2 = [1, 1, 3, 4, 5, 6, 7, 8]

set_1 = set(list_1)
print(f"set_1 = {set_1}")
set_2 = set(list_2)
print(f"set_2 = {set_2}")

# Merge list_1 and list_2 into list_12
list_1.extend(list_2)
list_12 = sorted(list_1)

print(f"list_12 = {list_12}")

set_12 = set_1.union(set_2)
print(f"set_12 = {set_12}")
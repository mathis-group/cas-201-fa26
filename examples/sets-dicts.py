# Lists and Tuples
my_list = [1, 2, 3, "a", "b", "c", 1,2,3, "c"]

my_list[4] = "B"

# print(f"my_list[4] = {my_list[4]}")

my_tuple = (1, 2, 3, "a", "b", "c")
# print(f"my_tuple[4] = {my_tuple[4]}")

# Sets
my_set = {1, 2, 3, "a", "b", "c", 1, "a", "a", "c", "c", "c"}
#print(f"my_set = {my_set}")
my_set.add(10)
my_set.add("B")
# print(f"my_set = {my_set}")

my_list_from_set = list(my_set)
#print(f'my_list_from_set = {my_list_from_set}')

my_set_from_list = set(my_list)
#print(f"my_set_from_list = {my_set_from_list}")

a_set = {1, 2, "b"}
b_set = {1, 2, 3, "a", "c"}

intersection_ab = a_set.intersection(b_set)
#print(f"intersection_ab = {intersection_ab}")
union_ab = a_set.union(b_set)
#print(f"union_ab = {union_ab}")

# Dictionaries
my_dict = {"name":"Cole", "birthday":"June-12", "age":34}
print(f'my_dict["name"] = {my_dict["name"]}')
print(f'my_dict["birthday"] = {my_dict["birthday"]}')
print(f'my_dict["age"] = {my_dict["age"]}')

my_dict["age"] = 35

# print(f'my_dict["age"] = {my_dict["age"]}')

my_dict["wish_list"] = ["ebike", "new phone", "sleep in"]
print(f"my_dict = {my_dict}")

my_dict["children"] = {"name": "Thing1", "birthday":"01-01", "age":3}
# print(f"my_dict = {my_dict}")

my_keys = my_dict.keys()
print(f"my_keys = {my_keys}")

children_wish_list = my_dict["children"].get("wish_list", "NA")
print(f"children_wish_list = {children_wish_list}")
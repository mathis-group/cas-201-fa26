
# Define some empty lists
x = []
y = [] # x^2
# Iterate over a range (in this case 10)
for i in range(10):
    # New data
    new_x = i 
    x.append(new_x) # append to list (attach it the end)
    # New data
    new_y = i**2 # ** is exponetentiation
    y.append(new_y) # append to the list


# print(x)
# print(y)
def f_to_c(temp_f):
    temp_c = (temp_f - 32) / 1.8
    return temp_c

daily_temps_f = (110, 109, 113, 101, 100, 99, 105, 99, 98, 97, 95, 100, 110, 101)
for q in daily_temps_f:
    print(f"The daily temp in F is {q}, and in C is {f_to_c(q)}")

print("Done.")
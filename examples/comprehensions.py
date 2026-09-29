
N_things = 10

xs = [i for i in range(N_things)]
ys = [i**2 for i in range(N_things)]
zs = [2*x + 10 for x in xs]

f_of_x = {str(x):x**2 for x in range(1, 15)}


print(f"xs = {xs}")
print(f"ys = {ys}")
print(f"zs = {zs}")

print(f"f_of_x = {f_of_x}")


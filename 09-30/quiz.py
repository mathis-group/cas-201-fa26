N = 37

xs = []
x = 0

while x**2 < N:
    xs.append(x**2)
    x += 1

ys = []
for x in xs:
    y = x-4
    ys.append(x-4)

#ys = [x - 2 for x in xs]

print(f"xs = {xs}")
print(f"ys = {ys}")
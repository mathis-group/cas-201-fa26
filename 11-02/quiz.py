import numpy as np

arr = np.zeros(5)

arr[1] = 10.0
arr[2] = 11
arr[3] = 12
arr[4] = 13

b = arr.sum()
c = len(arr)

print(f"b = {b}")
print(f"c = {c}")


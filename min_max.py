import numpy as np

# pehli line -> N aur M
n, m = map(int, input().split())

# agli N lines -> array ke rows
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# numpy array banalo
my_array = np.array(arr)

min_arr = np.min(my_array , axis=1)
max_arr = np.max(min_arr)
print("Minimum array",min_arr)
print("Maximum array", max_arr)

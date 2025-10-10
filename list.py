arr = [5 , 7, 8, 3, 9, 20]
min_value = min(arr)
minus_arr = []
for i in arr:
    minus = i - min_value
    if minus == 0:
        continue
    else:
        minus_arr.append(minus)

print(f"Final list of Number is {minus_arr}")